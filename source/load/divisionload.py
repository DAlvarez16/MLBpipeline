
from .database import engine
from sqlalchemy import text


def load_divisions(transformed_divisions):
    
    with engine.begin() as connection:
        for division in transformed_divisions:
            connection.execute(
            text("""
                INSERT INTO division (division_id, division_name, league_id, division_abbreviation)
                VALUES (:division_id, :division_name, :league_id, :division_abbreviation)
                ON CONFLICT (division_id)
                DO  UPDATE SET
                 division_name = EXCLUDED.division_name,
                 league_id = EXCLUDED.league_id,
                 division_abbreviation = EXCLUDED.division_abbreviation;

        
            """),
            {
                "division_id": division["division_id"],
                "division_name": division["division_name"],
                "league_id": division["league_id"],
                "division_abbreviation": division["division_abbreviation"]
                
            }
        )