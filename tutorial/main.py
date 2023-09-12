# Blog: https://fastapi.tiangolo.com/tutorial/first-steps/

from fastapi import FastAPI

# instance of Fast API
app = FastAPI()


# $uvicorn main:app --reload
# main- file name & app: instance of Class

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Basic Operations
# @app.post() - POST: to create data.
# @app.get() - GET: to read data.
# @app.put() - PUT: to update data.
# @app.delete() - DELETE: to delete data.

@app.get("/hello")
def read_hello():
    return {
        "message":"Hello welcome to the Fast API first GET API implimentaion.."
    }

# path

@app.get("/items/{item_id}/{section_id}")
def getItem(item_id:str,section_id: int):
    return {"item_id":item_id, "section_id":section_id}
# example : /items/p1/1

# Data Should be of given that type othervise get data validation error

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}



# Pydantic : For data validation

# Path Order should be like this : base > child > grand-childs

@app.get("/users")
def getUsers(self):
    pass

@app.get("/users/{user_id}/")
def getUser(user_id: str):
    pass

# https://fastapi.tiangolo.com/tutorial/path-params/#:~:text=path%20matches%20first.-,Predefined%20values,-%C2%B6