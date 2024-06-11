import pandera as pa
from pandera.typing import DataFrame, Series
from typing import Optional, Union

class AirbnbSchema(pa.SchemaModel):
    name: Series[str] = pa.Field(nullable=False)
    host_id: Series[int] = pa.Field(nullable=False)
    host_name: Series[str] = pa.Field(nullable=False)
    neighbourhood_group: Series[str] = pa.Field(nullable=False)
    neighbourhood: Series[str] = pa.Field(nullable=False)
    room_type: Series[str]
    price: Series[float] = pa.Field(ge=14.0)
    minimum_nights: Series[int] = pa.Field(nullable=False, ge=1, le=1000)
    number_of_reviews: Series[int] = pa.Field(nullable=False)
    last_review: Series[str] = pa.Field(nullable=True)
    rating: Series[str] = pa.Field(nullable=True)
    bedrooms: Series[int]= pa.Field(nullable=True)
    beds: Series[int]
    baths: Series[str] = pa.Field(nullable=True)
    status_location: Series[str] = pa.Field(nullable=False)
    created_at: Series[str] = pa.Field(nullable=False)
    origin: Series[str] = pa.Field(nullable=False)

    
    class Config:
        coerce = True
        strict = False