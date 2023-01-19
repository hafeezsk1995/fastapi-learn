from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
app = FastAPI()

@app.get("/")
def index():
     return {"Hello": "World"}

# @app.get("/about")
# def about():
#     return {'data':'about page'}

@app.get("/blog/publisher")
def comments(): #
    return {'publisher':1}

@app.get("/blog/{id}")
def show(id:int):
    #
    return {'data':id}



@app.get("/blog/{id}/comments")
def comments(id): #
    return {'comments':id}


# query parameters

@app.get("/blog/")
def display(limit:int = 10, published:bool = True, sort: Optional[str] = None):
    if published:
        print("published")
    else:
        print("UN published")    

@app.get("/about")
def display(limit:int, published:bool = True, sort: Optional[str] = None):
    if published:
        print("published")
    else:
        print("UN published")   


class Blog(BaseModel):
    title :str
    desc :Optional[str] = None
    published :bool

# create methods
@app.post("/create")
def create_blog(request:Blog):
    return "Blog is created with title"

# CHANGING PORT number
if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=9000)

    

