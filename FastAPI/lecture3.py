from fastapi import FastAPI 
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()
add_new_in_this_post = [{"id":1,"name":"jay","title":"FastAPI","content":"Writing FastAPI"},
                        {"id":2,"name":"Devarsh","title":"PostgreSQL","content":"Learning DataBase"},
                        {"id":3,"name":"Talha","title":"Django","content":"Making Full stack App"}]

class post(BaseModel):
    title : str
    content: str
    id : int
    name : Optional[str]
    

@app.get("/")
def root():
    return {"Message":"This is a Third Lecture"}

@app.post("/createPost")
def createPost(post: post):
    print(post.title)
    print(post.id)
    createPost = post.dict()
    return {"data": createPost}

@app.post("/appendPost")
def appendPost(post:post):
    existing_post = post.dict()
    existing_post['id'] = randrange(1,10000)
    add_new_in_this_post.append(existing_post)
    return {"data":add_new_in_this_post}
            