from fastapi import FastAPI,Response
from pydantic import BaseModel
from fastapi.params import Body

app = FastAPI()

posts = [{"title":"abc","content":"xyz","id":123},{"title":"abcrrr","content":"xyrrrz","id":12 }]

# if here i declare anyone then it will become optional
class Post(BaseModel):
    title:str
    content:str
    id:int = None

@app.get("/")
def root():
    return {"message":"hello world reduce polution and make world clean"}


@app.get("/posts")
def get_post():
    return {"message":posts} # we give here array fastapi automatically convert it into json format or serialize it

# add new entry
@app.post("/create_post")
def create_post(po : Post):
    posts.append(po.dict())
    print(posts)
    return "successfully done"

# retreive one individual

@app.get("/post/{_id}")
def create_post(_id:int,response:Response):
    print(_id)
    tmp = find_post(_id)
    if not tmp:
        response.status_code = 404
        return 
    return {"message":tmp}

def find_post(id):
    if len(posts) == id:
        return None
    else:
        return posts[id]

def find_index(id):
    print(id)
    for i,p in enumerate(posts):
        print("------------",i,"------",p,"-----------")
        if id == p["id"]:
            print("-----",i,"--------")
            return i
        
@app.delete("/delete/{id}")
def post_delte(id : int):
    i = find_index(id)
    posts.pop(i)
    return "successsfully deleted"

@app.put("/update/{id}")
def update(id:int,data:Post):
    index = find_index(id)
    if index == None:
        return "your record are not available "
    tmp = data.dict()
    posts[index] = tmp
    return "record is upated"