import requests
import json

venueurl = 'https://statsapi.mlb.com/api/v1/venues'
venues = json.loads(requests.get(venueurl).text)    

print(json.dumps(venues, indent=4))