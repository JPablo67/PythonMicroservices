from fastapi import APIRouter, Body, HTTPException
from schemas.movie_schema import Movie

movie_route = APIRouter()

@movie_route.post("/")
def create_movie(movie: Movie = Body(...)):
    try:
        # Insert movie creation logic here
        return movie
    except Exception as e:
        return {"error": str(e)}

@movie_route.get("/{id}")
def get_movie(id: int):
    try:
        # Insert logic to fetch a movie by ID
        return {"movie": "Movie details here"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Movie not found")

@movie_route.put("/{id}")
def update_movie(id: int, movie: Movie = Body(...)):
    try:
        # Insert movie update logic here
        return {"movie": "Updated movie details here"}
    except Exception as e:
        return {"error": str(e)}

@movie_route.delete("/{id}")
def delete_movie(id: int):
    try:
        # Insert logic to delete a movie by ID
        return {"message": "Movie deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Movie not found")