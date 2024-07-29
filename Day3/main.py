from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Body

app = FastAPI()

# if here i declare anyone then it will become optional
class Post(BaseModel):
    name:str
    age:int = 0 #now this is optional

# now using our own schema using pydantic
@app.post("/")
async def create_item(new_post:Post):
    print(new_post)
    return "hello this is post request geting request body"


# extracting using body
# @app.post("/")
# async def create_item(payLoad : dict = Body(...)):
#     print(payLoad)
#     print(type(payLoad))
#     if(payLoad["name"] == "sharyar khan"):
#         return "you are allowed"
    
#     return "hello this is post request geting request body"