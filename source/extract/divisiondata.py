import requests 
import json
def get_divisions():
    divisionsurl = 'https://statsapi.mlb.com/api/v1/divisions'
    divisions = json.loads(requests.get(divisionsurl).text)
    return divisions


