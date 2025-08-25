from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class post(BaseModel):
    title: str
    content: str
    id :int
    name: Optional[str]
    
data1 = [{"id":1,"name":"jay","title":"FastAPI","content":"Writing FastAPI"},
         {"id":2,"name":"Devarsh","title":"PostgreSQL","content":"Learning DataBase"},
         {"id":3,"name":"Talha","title":"Django","content":"Making Full stack App"}]

@app.get("/")
def root ():
    return {"Message": "This is a Lecture 4 of user ID dynamic Post"}

@app.post("/createPost")
def createPost (Post: post):
    return{"Message":Post}

def find_post(id):
    for iterative_post in data1:
        if iterative_post['id'] == id:
            return iterative_post
        
@app.post("/posts/latest")
def get_latest_post():
    latest_post = data1[len(data1)-1]
    return {"latest_post": latest_post}
    
@app.post("/posts/{id}")
def get_post(id: int): # this can check user can give integer value and accidently not give then not show sever error
    post = find_post(id)
    return {"post Detail": post}

# python is a interpreted language so we nned to carefull will writing routing like below code give error cause its above it try to match like latest to try in convert integer but fails 

# @app.post("/posts/latest")
# def get_latest_post():
#     latest_post = data1[len(data1)-1]
#     return {"latest_post": latest_post}
