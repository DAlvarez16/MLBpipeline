import requests
import json

def get_venues():
    venueurl = 'https://statsapi.mlb.com/api/v1/venues'
    venues = json.loads(requests.get(venueurl).text)
    return venues


