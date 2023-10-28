from fastapi import FastAPI

from routes import auth_router
from database.database import engine
from models.user_model import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router.router)
