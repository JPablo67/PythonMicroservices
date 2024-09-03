from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    id: int
    street: str
    city: str
    state: str
    zip_code: str
    country: str