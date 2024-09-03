from fastapi import APIRouter, Body, HTTPException
from models.book import Book

book_route = APIRouter()

@book_route.post("/")
def create_book(book: Book = Body(...)):
    try:
        # Insert book creation logic here
        return book
    except Exception as e:
        return {"error": str(e)}

@book_route.get("/{id}")
def get_book(id: int):
    try:
        # Insert logic to fetch a book by ID
        return {"book": "Book details here"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Book not found")

@book_route.put("/{id}")
def update_book(id: int, book: Book = Body(...)):
    try:
        # Insert book update logic here
        return {"book": "Updated book details here"}
    except Exception as e:
        return {"error": str(e)}

@book_route.delete("/{id}")
def delete_book(id: int):
    try:
        # Insert logic to delete a book by ID
        return {"message": "Book deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Book not found")