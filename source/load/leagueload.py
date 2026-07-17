from .database import engine
from sqlalchemy import text




def load_leagues(transformed_leagues):

    with engine.begin() as connection:
        for league in transformed_leagues:
            connection.execute(
            text("""
                INSERT INTO league (league_id, league_name, league_abbreviation)
                VALUES (:league_id, :league_name, :league_abbreviation)
                ON CONFLICT (league_id)
                DO UPDATE SET
                 league_name = EXCLUDED.league_name,
                 league_abbreviation = EXCLUDED.league_abbreviation;
                 
            """),
            {
                "league_id": league["id"],
                "league_name": league["name"],
                "league_abbreviation": league["abbreviation"]
            }
        )
            

