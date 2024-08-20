from fastapi import APIRouter, Body
from schemas.user_schema import User

user_route = APIRouter()

#Create User
@user_route.post("/")
def create_users(user: User = Body(...)):
    try:
        return user
    except Exception as e:
        print(e)
        return {"error": str(e)}
    
# Get User by ID
@user_route.get("/{id}")
def get_user(id: int):
    try:
        # Logic to retrieve user by ID
        
        user = {"id": id, "username": "sample_user", "email": "user@example.com"}  # Placeholder response
        return user
    except Exception as e:
        raise HTTPException(status_code=404, detail="User not found")

# Update User by ID
@user_route.put("/{id}")
def update_user(id: int, user: User = Body(...)):
    try:
        # Logic to update the user by ID
        
        updated_user = {"id": id, "username": user.username, "email": user.email}
        return updated_user
    except Exception as e:
        return {"error": str(e)}

# Delete User by ID
@user_route.delete("/{id}")
def delete_user(id: int):
    try:
        # Logic to delete the user by ID
        
        return {"message": "User deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="User not found")