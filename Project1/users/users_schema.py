from pydantic import BaseModel,EmailStr
from typing import Optional
# from datetime import datetime


class users_create(BaseModel):
    name :str
    email:EmailStr
    password : Optional[str] = None
    
class user_out(BaseModel):
    id : int
    name:str
    email:EmailStr