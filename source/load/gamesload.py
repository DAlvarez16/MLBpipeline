from .database import engine
from sqlalchemy import text


def load_games(transformed_games):
 
    with engine.begin() as connection:
        for game in transformed_games:
            connection.execute(
            text("""
                INSERT INTO games (gamesID, gameDate, homeTeamId, awayTeamId, homeTeamScore, awayTeamScore, venueId,status)
                VALUES (:game_id, :game_date, :home_team_id, :away_team_id, :home_team_score, :away_team_score, :venue_id, :status)
                ON CONFLICT (gamesID)
                DO UPDATE SET             
                gameDate = EXCLUDED.gameDate,
                homeTeamId = EXCLUDED.homeTeamId,
                awayTeamId = EXCLUDED.awayTeamId,
                homeTeamScore = EXCLUDED.homeTeamScore,
                awayTeamScore = EXCLUDED.awayTeamScore,
                venueId = EXCLUDED.venueId,
                status = EXCLUDED.status;
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
            
