from fastapi import APIRouter, Body, HTTPException
from models.address import Address

address_route = APIRouter()

@address_route.post("/")
def create_address(address: Address = Body(...)):
    try:
        # Insert address creation logic here
        return address
    except Exception as e:
        return {"error": str(e)}

@address_route.get("/{id}")
def get_address(id: int):
    try:
        # Insert logic to fetch an address by ID
        return {"address": "Address details here"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Address not found")

@address_route.put("/{id}")
def update_address(id: int, address: Address = Body(...)):
    try:
        # Insert address update logic here
        return {"address": "Updated address details here"}
    except Exception as e:
        return {"error": str(e)}

@address_route.delete("/{id}")
def delete_address(id: int):
    try:
        # Insert logic to delete an address by ID
        return {"message": "Address deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Address not found")