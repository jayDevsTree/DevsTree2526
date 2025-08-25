from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

class samplePost(BaseModel):
    title : str
    content: str
    
class samplePost2(BaseModel):
    title :str
    content: str
    published : bool = True
    rating : Optional[int] = None

app = FastAPI()

@app.get("/")
def root():
    return {"Message": "This is a Root path"}

@app.get("/about")
def aboutPage():
    return {"Message": "This is a About Page"}

@app.post("/createPostRequest")
def createPost(body_data_fetch : dict = Body(...)):
    print(body_data_fetch)
    return{"Message":"Making post requests"}

@app.post("/bodypost")
def createSamplePost(fetch_body : dict = Body(...)):
    return {"New_post" : f"this is a new post {fetch_body['title']}{fetch_body['content']}"}

@app.post("/pydanticSample")
def pydanticPostExample(new_post :samplePost):
    print("whole post:" ,new_post)
    print(new_post.title)
    print(new_post.content)
    return {"New_post":"Post"}

@app.post("/defalutValuesPydantic")
def defaultPydanticValues(post : samplePost2):
    # print(post.title)
    # print(post.content)
    # print(post.published)
    # print(post.rating)
    print(post)
    print(post.dict())
    return {'latest_post':"defaultPydanticValues values are shown"}