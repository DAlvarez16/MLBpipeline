from .database import engine
from sqlalchemy import text

def load_teams(transformed_teams):
    
    with engine.begin() as connection:
        for team in transformed_teams:
            connection.execute(
            text("""
                INSERT INTO teams (team_id, team_name, team_code, location_name, venue_id, division_id, league_id)
                VALUES (:team_id, :team_name, :team_code, :location_name, :venue_id, :division_id, :league_id)
                ON CONFLICT (team_id)
                DO UPDATE SET
                 team_name = EXCLUDED.team_name,
                 team_code = EXCLUDED.team_code,
                 location_name = EXCLUDED.location_name,
                 venue_id = EXCLUDED.venue_id,
                 division_id = EXCLUDED.division_id,
                 league_id = EXCLUDED.league_id;
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