from pydantic import BaseModel
from typing import Optional

class Car(BaseModel):
    id: int
    make: str
    model: str
    year: int
    vin: str 
    color: Optional[str] = None
