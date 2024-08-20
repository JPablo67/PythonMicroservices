from fastapi import FastAPI , Body
from starlette.responses import RedirectResponse

#App routes
from routes.user import user_route

#App instance
app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse(url='/docs')

# PROVIDERS
app.include_router(user_route, prefix="/users", tags=["Usuarios"])


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