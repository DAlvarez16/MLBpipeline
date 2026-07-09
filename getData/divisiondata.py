import requests 
import json

divisionsurl = 'https://statsapi.mlb.com/api/v1/divisions'
divisions = json.loads(requests.get(divisionsurl).text)

for division in divisions['divisions']:
    if division['league']['id'] in [103, 104]:
        print(f"{division['name']} -- {division['abbreviation']  } ")  