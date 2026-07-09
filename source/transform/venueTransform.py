import requests
import json

def transform_venues(venues):
    transformed_venues = []
    for venue in venues['venues']:
        transformed_venue = {
            'id': venue['id'],
            'name': venue['name'],
        }
        transformed_venues.append(transformed_venue)
    return transformed_venues