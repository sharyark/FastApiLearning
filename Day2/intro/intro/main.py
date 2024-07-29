from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    # return {"message": "Hello Worldsss"}
    return "<h1>hello</h1>"


# @app.post("/post")
# async def root():
#     return {"message": "posted successfully!"}
    # return "<h1>hello</h1>"
# path parameter
@app.get("/post/{_id}")
async def root(_id:int):
    return {"message1": "posted successfully!",'message':_id}
    # return "<h1>hello</h1>"



# Query parameter 

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"},{"item_name": "Baz"},{"item_name": "Baz"}]


@app.get("/item/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# required query parameter 
# when parameter is not declared then it is required
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item