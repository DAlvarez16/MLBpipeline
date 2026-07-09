import requests 
import json

def get_leagues():
    leagueurl = 'https://statsapi.mlb.com/api/v1/league'
    league = json.loads(requests.get(leagueurl).text)
    return league

