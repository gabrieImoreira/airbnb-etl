from sqlalchemy import Column, Integer, BigInteger, Float, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AirbnbRooms(Base):
    __tablename__ = 'airbnb_rooms'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    host_id = Column(BigInteger, nullable=False)
    host_name = Column(String, nullable=False)
    neighbourhood_group = Column(String, nullable=False)
    neighbourhood = Column(String, nullable=False)
    room_type = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    currency = Column(String, nullable=False)
    minimum_nights = Column(Integer, nullable=False)
    number_of_reviews = Column(Integer, nullable=False)
    last_review = Column(TIMESTAMP, nullable=True)
    rating = Column(Float, nullable=True)
    bedrooms = Column(Integer, nullable=True)
    beds = Column(Integer, nullable=True)
    baths = Column(String, nullable=True)
    status_location = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    origin = Column(String, nullable=True) 

    def __repr__(self):
        return (
            f"<AirbnbRooms(id={self.id}, name={self.name}, host_id={self.host_id}, "
            f"host_name={self.host_name}, neighbourhood_group={self.neighbourhood_group}, "
            f"neighbourhood={self.neighbourhood}, room_type={self.room_type}, "
            f"price={self.price}, currency={self.currency}, minimum_nights={self.minimum_nights}, "
            f"number_of_reviews={self.number_of_reviews}, last_review={self.last_review}, "
            f"rating={self.rating}, bedrooms={self.bedrooms}, beds={self.beds}, "
            f"baths={self.baths}, created_at={self.execution_date}, origin={self.origin})>"
        )
