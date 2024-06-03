from src.tools.db.postgresql import PostgreSQLConnection
import polars as pl

class CSVCollector:
    def __init__(self):
        pass

    def main(self):
        print("Hello from CSVCollector")
        df = self.get_data("./data/new_york_listings_2024_api.csv")
        self.transform_data(df)
        
        # db = PostgreSQLConnection()
        # rooms = db.get_rooms()
        # for room in rooms:
        #     print(room)
    
    def get_data(self, filename):
        df = pl.read_csv(filename)
        return df

    def transform_data(self):
        pass

    def load_data(self):
        pass
        