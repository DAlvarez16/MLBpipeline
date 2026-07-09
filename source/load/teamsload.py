import requests
from sqlalchemy import create_engine
from sqlalchemy import text
import json
from dotenv import load_dotenv
import os

def load_teams(transformed_teams):
    load_dotenv()

    USER = os.getenv('DB_USER')
    PASSWORD = os.getenv('DB_PASSWORD')
    HOST = 'localhost'
    PORT = 5432
    DB_NAME = os.getenv('DB_NAME')

    conexion_string = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    engine = create_engine(conexion_string)

    with engine.begin() as connection:
        for team in transformed_teams:
            connection.execute(
            text("""
                INSERT INTO teams (team_id, team_name, team_code, location_name, venue_id, division_id, league_id)
                VALUES (:team_id, :team_name, :team_code, :location_name, :venue_id, :division_id, :league_id)
                ON CONFLICT (team_id)
                DO NOTHING;
            """),
            {
                "team_id": team["id"],
                "team_name": team["name"],
                "team_code": team["team_code"],
                "location_name": team["location_name"],
                "venue_id": team["venue_id"],
                "division_id": team["division_id"],
                "league_id": team["league_id"],
                
            }
        )