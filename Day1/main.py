# from datetime import datetime

# from pydantic import BaseModel


# class User(BaseModel):
#     id: int
#     name: str = "John Doe"
#     signup_ts: datetime | None = None
#     friends: list[int] = []


# external_data = {
#     "id": "123",
#     "signup_ts": "2017-06-01 12:22",
#     "friends": [1, "2", b"3"],
# }
# user = User(**external_data)
# print(user)
# # > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
# print(user.id)
# # > 123




# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel

# class Person(BaseModel):
#     name: str
#     age: int
#     hair_color: str
#     eye_color: str
#     nose_shape: str

# app = FastAPI()

# # Configure CORS
# app.add_middleware(
#     CORSMiddleware,
#     # allow_origins=["http://localhost:3000"],  # Allow your React origin here
#     allow_origins=["*"],  # Allow your React origin here
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# person_data = Person(
#     name="Sharyar Khan",
#     age=23,
#     hair_color="Black",
#     eye_color="Brown",
#     nose_shape="Tilde"
# )

# @app.get("/getdata")
# def get_data():
#     return person_data.dict()






















from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}