import requests
from sqlalchemy import create_engine
from sqlalchemy import text
import json
from dotenv import load_dotenv
import os

def load_divisions(transformed_divisions):
    load_dotenv()

    USER = os.getenv('DB_USER')
    PASSWORD = os.getenv('DB_PASSWORD')
    HOST = 'localhost'
    PORT = 5432
    DB_NAME = os.getenv('DB_NAME')

    conexion_string = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    engine = create_engine(conexion_string)

    with engine.begin() as connection:
        for division in transformed_divisions:
            connection.execute(
            text("""
                INSERT INTO division (division_id, division_name, league_id, division_abbreviation)
                VALUES (:division_id, :division_name, :league_id, :division_abbreviation)
                ON CONFLICT (division_id)
                DO NOTHING;
            """),
            {
                "division_id": division["division_id"],
                "division_name": division["division_name"],
                "league_id": division["league_id"],
                "division_abbreviation": division["division_abbreviation"]
            }
        )