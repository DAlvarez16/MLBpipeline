import requests
from sqlalchemy import create_engine
from sqlalchemy import text
import json
from dotenv import load_dotenv
import os

def load_venues(transformed_venues):
    load_dotenv()

    USER = os.getenv('DB_USER')
    PASSWORD = os.getenv('DB_PASSWORD')
    HOST = 'localhost'
    PORT = 5432
    DB_NAME = os.getenv('DB_NAME')

    conexion_string = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    engine = create_engine(conexion_string)

    with engine.begin() as connection:
        for venue in transformed_venues:
            connection.execute(
            text("""
                INSERT INTO venue (venue_id, venue_name)
                VALUES (:venue_id, :venue_name)
                ON CONFLICT (venue_id)
                DO NOTHING;
            """),
            {
                "venue_id": venue["id"],
                "venue_name": venue["name"],
                
            }
        )
    