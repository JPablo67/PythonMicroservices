from fastapi import APIRouter, Body
from schemas.user_schema import User

user_route = APIRouter()

@user_route.post("/")
def create_users(user: User = Body(...)):
    try:
        return user
    except Exception as e:
        print(e)
        return {"error": str(e)}
    
