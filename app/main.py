from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor # Usual pg lib returns only valus,  but this will retun with coln name as py dict
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from .routers import posts, users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
 
while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='2515',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful!")
        break

    except Exception as error:
        print("Connecting to Database failed")
        print("Error:",error)
        time.sleep(2)

# post to be stored in data base
my_posts = [{"title":"title of post 1", "content": "content of post 1","id":1},
{"title":"Favorite Food", "content": "I Like Pizza","id":2}]

def find_post(id):
    for post in my_posts:
        if post['id']==id:
            return post
def find_index_post(id): 
    for i,post in enumerate(my_posts):
        if post['id']==id:
            return i

app.include_router(posts.router)
app.include_router(users.router)

# request Get method url: "/"
@app.get("/")
def root():
    return {"message": "Hello world"}
    

###########################################################################################################

