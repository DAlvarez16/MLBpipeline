import requests
import json

def transform_teams(teams):
    transformed_teams = []
    for team in teams['teams']:
        transformed_team = {
            'id': team['id'],
            'name': team['name'],
            'team_code': team['teamCode'],
            'location_name': team['locationName'],
            'venue_id': team['venue']['id'],
            'division_id': team['division']['id'],
            'league_id': team['league']['id'],
        }
        transformed_teams.append(transformed_team)
    return transformed_teams