from pydantic import BaseModel
from datetime import date

class Order(BaseModel):
    id: int
    user_id: int
    item_id: int
    total_amount: float
    status: str
    date: date
