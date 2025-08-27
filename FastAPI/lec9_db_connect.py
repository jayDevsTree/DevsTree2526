from fastapi import FastAPI, status, Response, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os
import time


load_dotenv("db.env")

app = FastAPI()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

while True:
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database Connection Successful")
        break
    except Exception as error:
        print("Database Connection Failed")
        print("Error:", error)
        time.sleep(2)
        



# data = [{"id":1,"name":"jay","title":"FastAPI","content":"Writing FastAPI"},
#     {"id":2,"name":"Devarsh","title":"PostgreSQL"},
#     {"id":3,"name":"Talha","title":"Django"}]

class postBase(BaseModel):
    # id:int
    title:str
    content:Optional[str] =None
    published: Optional[bool] = False
    # created_at:datetime = Field(default_factory=datetime.now)


@app.get("/")
def root():
    return {"Message": "This Code Perform CRUD in FastAPI"}

@app.get("/getAllPost")
def allPost():
    cursor.execute(""" SELECT * FROM posts """)
    posts = cursor.fetchall()

    return {"data": posts}

@app.post("/createPost")
def createPost(post:postBase):
    
    cursor.execute(""" INSERT INTO posts(title,content,published) 
                        VALUES(%s,%s,%s) RETURNING * """,(post.title,post.content,post.published))
    create_post = cursor.fetchone()
    conn.commit()
    
    return {"data":create_post}

    # post_dict = post.dict()
    # post_dict["id"] = randrange(1,10000)
    # data.append(post_dict)
    # return {"data": data}


# def get_dynamic_id(id):# this return object(dictionary) of that id in data
#     for post in data:
#         if post["id"] == id:
#             return post
#     return None

# def get_index(id):# this return index (starts from 0,1,2...) a number not whole object(dictonary)
#     for index,post in enumerate(data):
#         if post["id"]== id:
#             return index
#     return None

@app.get("/getPost/{id}",status_code=status.HTTP_200_OK)
def getPost(id:int):
    cursor.execute(""" SELECT * FROM posts WHERE id = %s """,(id,))
    get_post = cursor.fetchone()
    print(get_post)
    if get_post == None:
        raise HTTPException(status_code = 404,
                            detail = f"Post with id:{id} Not Found")
    return{"data":get_post}    

    # get_post = get_dynamic_id(id)
    # if get_post == None:
    #     raise HTTPException(status_code = 404,
    #                         detail = f"Post with id:{id} Not Found")
    # return{"data":get_post}    
    

@app.put("/updatePost/{id}")
def updatePost(id:int,post:postBase):
    cursor.execute(""" UPDATE posts SET title = %s,content = %s WHERE id = %s RETURNING *""",(post.title,post.content,id))
    update_post = cursor.fetchone()
    conn.commit()   
    if update_post == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail = f"Post with id:{id} does not Exists")
    return {"data": update_post}

    # index= get_index(id)
    # if index == None:
    #     raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
    #                         detail = f"Post with id:{id} does not Exists")
        
    # data[index] = post.dict()
    # return {"data": data}

@app.delete("/deletePost/{id}",status_code=status.HTTP_204_NO_CONTENT)
def deletePost(id:int):
    cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING *""",(id,))
    delete_post = cursor.fetchone()
    conn.commit()
    if delete_post == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail = f"Post with id:{id} does not Exists")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
        
    # delete_index = get_index(id)
    # if delete_index == None:
    #     raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
    #                         detail = f"Post with id:{id} does not Exists")
    # data.pop(delete_index)
    # return Response(status_code=status.HTTP_204_NO_CONTENT)



    

