from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]=None
    

@app.get("/users")
async def get_users():
    return users

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return 'Success'