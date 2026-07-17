from extract import *
from transform import *
from load import *

def run_pipeline():

    # LEAGUES
    leagues = get_leagues()
    transformed_leagues = transform_leagues(leagues)
    load_leagues(transformed_leagues)

    # DIVISIONS
    divisions = get_divisions()
    transformed_divisions = transform_division(divisions)
    load_divisions(transformed_divisions)

    # VENUES
    venues = get_venues()
    transformed_venues = transform_venues(venues)
    load_venues(transformed_venues)

    # TEAMS
    teams = get_teams()
    transformed_teams = transform_teams(teams)
    load_teams(transformed_teams)

    # GAMES
    games = get_games()
    transformed_games = transform_games(games, transformed_teams)
    load_games(transformed_games)

    # RECORDS
    teamseasonrecords = team_season_records(
        transformed_teams,
        transformed_games
    )
    load_team_season_records(teamseasonrecords)

    print("Data pipeline executed successfully!")