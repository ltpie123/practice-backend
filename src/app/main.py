from fastapi import FastAPI
from datetime import datetime, UTC

from app.core.config import settings
from app.core.database import Base, engine
from sqlalchemy import Column, Integer, Boolean, String, DateTime

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/register")
def register():
    return {"message": "Registered"}


@app.post("/token")
async def login_for_access_token():
    return {"message": "User Logged In Successfully"}


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password_hash = Column(String)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    verification_code = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now(UTC))
