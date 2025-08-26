from fastapi import FastAPI,status,Response,HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

data = [{"id":1,"name":"jay","title":"FastAPI","content":"Writing FastAPI"},
    {"id":2,"name":"Devarsh","title":"PostgreSQL"},
    {"id":3,"name":"Talha","title":"Django"}]

class post(BaseModel):
    id : int
    name: str
    title: str
    content: Optional[str] = None
    
@app.get("/")
def root():
    return{"Message":"This code Just represents Delete Opreation"}


def find_post_delete(id):
    for delete_post in data:
        if delete_post['id'] == id:
            return delete_post
        
@app.post("createPost")
def createPost(post : post)
    pass
    