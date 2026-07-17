from .database import engine
from sqlalchemy import text

def load_venues(transformed_venues):
    
    with engine.begin() as connection:
        for venue in transformed_venues:
            connection.execute(
            text("""
                INSERT INTO venue (venue_id, venue_name)
                VALUES (:venue_id, :venue_name)
                ON CONFLICT (venue_id)
                DO UPDATE SET
                 venue_name = EXCLUDED.venue_name;
            """),
            {
                "venue_id": venue["id"],
                "venue_name": venue["name"],
                
            }
        )
    