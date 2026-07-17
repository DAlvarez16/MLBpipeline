import requests
import json
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy import text

load_dotenv()

def load_games(transformed_games):
    USER = os.getenv('DB_USER')
    PASSWORD = os.getenv('DB_PASSWORD')
    HOST = 'localhost'
    PORT = 5432
    DB_NAME = os.getenv('DB_NAME')

    conexion_string = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    engine = create_engine(conexion_string)

    with engine.begin() as connection:
        for game in transformed_games:
            connection.execute(
            text("""
                INSERT INTO games (gamesID, gameDate, homeTeamId, awayTeamId, homeTeamScore, awayTeamScore, venueId,status)
                VALUES (:game_id, :game_date, :home_team_id, :away_team_id, :home_team_score, :away_team_score, :venue_id, :status)
                ON CONFLICT (gamesID)
                DO NOTHING;
            """),
            {
                "game_id": game["gameID"],
                "game_date": game["gameDate"],
                "home_team_id": game["homeTeamId"],
                "away_team_id": game["awayTeamId"],
                "home_team_score": game["homeScore"],
                "away_team_score": game["awayScore"],
                "venue_id": game["venueId"],
                "status": game["status"]
            }
        )
            
