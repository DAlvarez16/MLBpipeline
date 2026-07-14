import requests 
import json

def get_teams():
    teamsurl = 'https://statsapi.mlb.com/api/v1/teams?sportId=1'
    teams = json.loads(requests.get(teamsurl).text)
    return teams



