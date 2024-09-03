from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: int
    title: str
    author: str
    isbn: str
    published_year: int
    genre: Optional[str] = None
