from pydantic import BaseModel, EmailStr
from typing import List

class User(BaseModel):
    name: str
    email: EmailStr
    age: int
    country: str
    interests: List[str]
