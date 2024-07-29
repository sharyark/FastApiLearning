from fastapi import FastAPI
from fastapi import Path
from fastapi import HTTPException
from pydantic import BaseModel
import sys
sys.path.append("/home/sharyar_khan/Desktop/FastAPI+SQL/Day5_DBs/app")

from db import get_connection, close_connection


# Initialize FastAPI app
app = FastAPI()

# get any of according to id
@app.get("/getone/{id}")
async def get_one(id: int = Path(..., title="The ID of the row to fetch")):
    # Get a database connection
    connection = get_connection()

    if connection:
        try:
            # Create a cursor object
            cursor = connection.cursor()

            # Execute a SQL query with a parameterized query to prevent SQL injection
            cursor.execute("SELECT * FROM posts WHERE id = %s LIMIT 1", (id,))

            # Fetch the first row
            row = cursor.fetchone()

            if row:
                return row
            else:
                return {"message": f"Row with ID {id} not found."}

        finally:
            # Close the cursor
            cursor.close()

            # Close the connection
            close_connection(connection)
    else:
        return {"message": "Unable to connect to the database."}



# get first one
@app.get("/getone")
async def get_one():
    # Get a database connection
    connection = get_connection()

    if connection:
        try:
            # Create a cursor object
            cursor = connection.cursor()

            # Execute a SQL query
            cursor.execute("SELECT * FROM posts LIMIT 1")

            # Fetch the first row
            row = cursor.fetchone()

            return row

        finally:
            # Close the cursor
            cursor.close()

            # Close the connection
            close_connection(connection)
    else:
        return {"message": "Unable to connect to the database."}


import logging

logger = logging.getLogger(__name__)

class Post(BaseModel):
    title: str
    content: str
    published: bool = False

class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool = False

@app.post("/add_post")
async def add_post(post: Post):
    # Get a database connection
    connection = get_connection()

    if connection:
        try:
            # Create a cursor object
            cursor = connection.cursor()

            # Execute a SQL query to insert a new row
            cursor.execute("INSERT INTO posts (id, title, content, published) VALUES (%s, %s, %s, %s)", (post.id, post.title, post.content, post.published))

            # Commit the transaction
            connection.commit()

            # Fetch the newly inserted row
            cursor.execute("SELECT * FROM posts ORDER BY id DESC LIMIT 1")
            new_row = cursor.fetchone()

            return new_row

        except Exception as e:
            # Log the error message
            logger.error(f"Failed to add post: {e}")

            # Rollback the transaction on error
            connection.rollback()
            raise HTTPException(status_code=500, detail="Failed to add post.")

        finally:
            # Close the cursor
            cursor.close()

            # Close the connection
            close_connection(connection)
    else:
        raise HTTPException(status_code=500, detail="Unable to connect to the database.")