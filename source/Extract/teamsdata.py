import requests 
import json

teamsurl = 'https://statsapi.mlb.com/api/v1/teams?sportId=1'
teams = json.loads(requests.get(teamsurl).text)

for team in teams['teams']:
    print(f"{team['name']} -- {team['teamCode']} -- {team['teamName']} -- {team['locationName']} -- {team['venue']['name']}")


