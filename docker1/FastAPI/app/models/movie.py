from pydantic import BaseModel
from typing import Optional

class Movie(BaseModel):
    id: int
    title: str
    director: str
    release_year: int
    genre: str
    rating: Optional[float] = None  # Optional if the movie hasn't been rated yet