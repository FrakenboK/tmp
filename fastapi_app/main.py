from fastapi import FastAPI
from contextlib import asynccontextmanager
import schemas
from database import database
import crud
import uvicorn

# @app.on_event is depricated, so added this:
@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate):
    user_id = await crud.create_user(user)
    return {"id": user_id, **user.model_dump()}

@app.get("/users/", response_model=list[schemas.User])
async def read_users():
    return await crud.get_users()

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=1337)