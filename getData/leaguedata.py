import requests 
import json

leagueurl = 'https://statsapi.mlb.com/api/v1/league'
league = json.loads(requests.get(leagueurl).text)

for league in league['leagues']:
    if league['id'] in [103, 104]:
        print(f"{league['name']} -- {league['abbreviation']}")
