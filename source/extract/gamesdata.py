import requests
import json

def get_games():
    url = 'https://statsapi.mlb.com/api/v1/schedule?sportId=1&season=2026&gameType=R'
    response = requests.get(url)
    return json.loads(response.text)

