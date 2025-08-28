from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime

class userCreate(BaseModel):
    email: EmailStr
    password: str
    
class userOut(BaseModel):
    id:int
    email: EmailStr
    created_at: datetime