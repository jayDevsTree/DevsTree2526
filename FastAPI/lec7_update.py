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
    for index,post_iteration in enumerate(data):
        if post_iteration['id'] == id:
            return index
    return None

def find_post(id):
    for post in data:
        if post["id"] == id:
            return post
        
@app.get("/getPost/{id}")
def getPost(id:int):
    get_dynamic_post = find_post(id)
    if not get_dynamic_post:
        raise HTTPException(status_code = 404,
                            detail = f"Post with id:{id} not Found")
    return {"data": get_dynamic_post}

@app.delete("/deletePost/{id}")
def deletePost(id:int):
    delete_post = find_post_delete(id)
    if delete_post == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail = f"Post with id:{id} does not Exists")
    data.pop(delete_post)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    


@app.put("/updatePost/{id}")
def updatePost(id:int,post:post):
    update_index = find_post_delete(id)
    if update_index == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail = f"Post with id:{id} does not Exists")
        
    data[update_index] = post.dict()
    return {"data": data}

@app.get("/getAllPost")
def getAllPost():
    return {"data": data}