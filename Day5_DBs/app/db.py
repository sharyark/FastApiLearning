import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_connection():
    try:
        # Connect to the database
        connection = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            cursor_factory=RealDictCursor
        )
        print("Connected to the database.")

        return connection

    except psycopg2.Error as e:
        print("Unable to connect to the database:", e)
        return None

def close_connection(connection):
    # Close the connection
    if connection:
        connection.close()
        print("Connection closed.")
