import requests
from sqlalchemy import create_engine
from sqlalchemy import text
import json
from dotenv import load_dotenv
import os

load_dotenv()

def load_leagues(transformed_leagues):
    USER = os.getenv('DB_USER')
    PASSWORD = os.getenv('DB_PASSWORD')
    HOST = 'localhost'
    PORT = 5432
    DB_NAME = os.getenv('DB_NAME')

    conexion_string = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    engine = create_engine(conexion_string)

    with engine.begin() as connection:
        for league in transformed_leagues:
            connection.execute(
            text("""
                INSERT INTO league (league_id, league_name, league_abbreviation)
                VALUES (:league_id, :league_name, :league_abbreviation)
                ON CONFLICT (league_id)
                DO NOTHING;
            """),
            {
                "league_id": league["id"],
                "league_name": league["name"],
                "league_abbreviation": league["abbreviation"]
            }
        )
            

