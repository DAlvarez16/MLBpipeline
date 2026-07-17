from .database import engine
from sqlalchemy import text

def load_team_season_records(teamseasonrecords):
    

    with engine.begin() as connection:
         connection.execute(text("""
            TRUNCATE TABLE team_season_records;
        """))
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