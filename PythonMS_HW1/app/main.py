from fastapi import FastAPI , Body
from starlette.responses import RedirectResponse

#App routes
from routes.user import user_route
from routes.order import order_route
from routes.movie import movie_route
from routes.car import car_route 
from routes.book import book_route
from routes.address import address_route

#App instance
app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse(url='/docs')

# PROVIDERS
app.include_router(user_route, prefix="/users", tags=["Usuarios"])
app.include_router(order_route, prefix="/orders", tags=["Orders"])    # Include order route
app.include_router(movie_route, prefix="/movies", tags=["Movies"])    # Include movie route
app.include_router(car_route, prefix="/cars", tags=["Cars"])          # Include car route
app.include_router(book_route, prefix="/books", tags=["Books"])       # Include book route
app.include_router(address_route, prefix="/addresses", tags=["Addresses"])  # Include address route

# @app.post("/")
# def read_root():
#     return {"Hello":"World"}

# @app.delete("/")
# def read_root():
#     return {"Hello":"World"}

# @app.put("/")
# def read_root():
#     return {"Hello":"World"}

# ####################################################

# @app.get("/users/")
# def read_user():
#     return {"user_id": "user_id"}

# @app.get("/users/{user_id}")
# def read_user(user_id:int):
#     return {"user_id": user_id}

# @app.post("/users/")
# def create_user(user: User = Body(...)):
#     return user