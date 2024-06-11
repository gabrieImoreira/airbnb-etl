from sqlalchemy.orm.session import Session as SessionBase
from src.tools.db.model import Base, AirbnbRooms
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import traceback
import os 

class PostgreSQLConnection:

    def __init__(self):
        self.host = os.getenv('POSTGRES_HOST')
        self.port = os.getenv('POSTGRES_PORT')
        self.user = os.getenv('POSTGRES_USER')
        self.password = os.getenv('POSTGRES_PASSWORD')
        self.database = os.getenv('POSTGRES_DB')

        self.session = self.__connect()

    def __connect(self):
        connection_string = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        engine = create_engine(connection_string, echo=False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        return Session()
    
    def get_rooms(self, **kwargs):
        # Criar uma query base
        query = self.session.query(AirbnbRooms)

        # Adicionar condições dinâmicas
        for key, value in kwargs.items():
            query = query.filter(getattr(Faturamento, key) == value)

        # Executar a query e retornar os resultados
        return query.all()

    def insert_room(self, name, host_id, host_name, neighbourhood_group, neighbourhood, room_type,
         price, currency, minimum_nights, number_of_reviews, last_review, rating, bedrooms,
         beds, baths, created_at, origin):
        
        existing_record = self.session.query(AirbnbRooms).filter_by(name=name, host_name=host_name).first()
        if existing_record:
            return False 

        client = AirbnbRooms()
        self.session.add(client)
        self.session.commit()
        return True 

    def update_room(self, name, host_name, **kwargs):
        try:
            # Filtrar os registros pelo cp e mes fornecidos
            register = self.session.query(Faturamento).filter_by(name=name, host_name=host_name).first()

            if registro:
                for key, value in kwargs.items():
                    setattr(register, key, value)

                self.session.commit()
                return True
            else:
                return False
        except SQLAlchemyError as e:
            print("Error during update:", e)
            self.session.rollback()
            return False
    
    def bulk_upsert_rooms(self, df):
        try:
            records = df.to_dict(orient='records')
            rooms = [AirbnbRooms(**record) for record in records]
            
            self.session.bulk_save_objects(rooms, update_changed_only=True)
            self.session.commit()
        except SQLAlchemyError as e:
            print("Error during bulk insert/update:", e)
            self.session.rollback()

            