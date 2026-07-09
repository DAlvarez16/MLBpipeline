import json
import requests

def transform_division(division):
    transformed_division = []

    for division in division['divisions']:
        if division['league']['id'] in [103, 104]:
            transformed_division.append({
            'division_id': division['id'],
            'division_name': division['name'],
            'league_id': division['league']['id'],
            'division_abbreviation': division['abbreviation']
            })
    return transformed_division

