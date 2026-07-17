from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy import text

load_dotenv()

def load_team_season_records(teamseasonrecords):
    USER = os.getenv('DB_USER')
    PASSWORD = os.getenv('DB_PASSWORD')
    HOST = 'localhost'
    PORT = 5432
    DB_NAME = os.getenv('DB_NAME')

    conexion_string = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    engine = create_engine(conexion_string)

    with engine.begin() as connection:
        for record in teamseasonrecords:

            connection.execute(
            text("""
                INSERT INTO team_season_records
                (team_id, wins, losses, home_wins, away_wins,
                home_losses, away_losses, total_games)
                VALUES
                (:team_id, :wins, :losses, :home_wins, :away_wins,
                :home_losses, :away_losses, :total_games)
                ON CONFLICT (team_id)
                DO NOTHING;
                """),
            {
                "team_id": record["team_id"],
                "wins": record["wins"],
                "losses": record["losses"],
                "home_wins": record["home_wins"],
                "away_wins": record["away_wins"],
                "home_losses": record["home_losses"],
                "away_losses": record["away_losses"],
                "total_games": record["total_games"]
            }
        )