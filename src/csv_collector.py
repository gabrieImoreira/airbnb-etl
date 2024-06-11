from src.tools.db.postgresql import PostgreSQLConnection
from src.tools.aws.s3_client import S3Client
from src.tools.schema import AirbnbSchema
from datetime import datetime
import pandera as pa
import pandas as pd
import os

class CSVCollector:
    def __init__(self):
        self.db = PostgreSQLConnection()
        self._aws = S3Client()

    def main(self):
        self.download_file()
        for file in os.listdir('data'):
            file = f'data/{file}'
            df = self.get_data(file)
            df = self.transform_data(df)
            self.load_data(df)
            self.clean_up(file)

    def download_file(self):
        files = self._aws.list_object('data/')
        for file in files:
            if file['Key'].endswith('.csv'):
                file = self._aws.download_file(file['Key'], file['Key'])
                if not file:
                    raise Exception('Error downloading file')
                break
    
    def clean_up(self, file):
        print('dilee', file)
        self._aws.move_object(file, f'data/processed/{file.split("/")[-1]}')
        os.remove(file)


    def get_data(self, filename):
        df = pd.read_csv(filename)
        return df 
    
    @pa.check_output(AirbnbSchema)
    def transform_data(self, df):
        df['origin'] = 'csv file'
        df['created_at'] = datetime.now()
        df['currency'] = 'USD'
        df['bedrooms'] = df['bedrooms'].replace({"Studio": 0}).astype(float)
        df['baths'] = df['baths'].replace({"Not specified": 0}).astype(float)

        # Remove leading and trailing whitespaces
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].str.strip()
        
        # Create a new column to store the status of the location
        df['status_location'] = df['rating'].apply(lambda x: 'New' if x.strip() == 'New' else ('Existing' if x.strip() == 'No rating' else x))
        
        # Replace the values of the rating column
        df['rating'] = df['rating'].replace({"New": 0, "No rating": 0})

        df = df.drop(columns=['id','latitude', 'longitude',
            'reviews_per_month', 'calculated_host_listings_count', 
            'availability_365', 'number_of_reviews_ltm', 'license'])
        
        return df

    def load_data(self, df):
        self.db.bulk_upsert_rooms(df)
        return True
            