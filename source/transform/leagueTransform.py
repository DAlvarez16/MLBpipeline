import requests 
import json

def transform_leagues(leagues):
    transformed_leagues = []
    for league in leagues['leagues']:
        transformed_league = {
            'id': league['id'],
            'name': league['name'],
            'abbreviation': league['abbreviation'],   
        }
        if league['id'] in [103, 104]:
            transformed_leagues.append(transformed_league)
    return transformed_leagues


