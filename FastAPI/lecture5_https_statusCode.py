from fastapi import FastAPI,Response,status,HTTPException
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
    
@app.get("/posts/{id}",status_code=status.HTTP_201_CREATED)
def get_post(id: int , response: Response): # this can check user can give integer value and accidently not give then not show sever error
    post = find_post(id)
    
    if not find_post(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} not found")
        
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id:{id} not found"}
    return {"post Detail": post}
