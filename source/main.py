import requests;
import json;
from sqlalchemy import create_engine;
from dotenv import load_dotenv;
import os;
from extract.leaguedata import get_leagues;
from extract.venuedata import get_venues;
from extract.divisiondata import get_divisions;
from extract.teamsdata import get_teams;
from extract.gamesdata import get_games;
from transform.gamesTransform import transform_games;
from transform.leagueTransform import transform_leagues;
from transform.venueTransform import transform_venues;
from transform.divisionTransform import transform_division;
from transform.teamsTransform import transform_teams;
from transform.leagueTransform import transform_leagues;
from transform.recordTransform import team_season_records;
from load.gamesload import load_games;
from load.leagueload import load_leagues;
from load.divisionload import load_divisions;
from load.teamsload import load_teams;
from load.venueload import load_venues;
from load.recordsload import load_team_season_records;

leagues = get_leagues();
transformed_leagues = transform_leagues(leagues);
load_leagues(transformed_leagues);

divisions = get_divisions();
transformed_divisions = transform_division(divisions);
load_divisions(transformed_divisions);

venues = get_venues();
transformed_venues = transform_venues(venues);
load_venues(transformed_venues);

teams = get_teams();
transformed_teams = transform_teams(teams);
load_teams(transformed_teams);

games = get_games();
transformed_games = transform_games(games,transformed_teams);
load_games(transformed_games);

teamseasonrecords= team_season_records(transformed_teams, transformed_games)
load_team_season_records(teamseasonrecords)


print("Data pipeline executed successfully!");