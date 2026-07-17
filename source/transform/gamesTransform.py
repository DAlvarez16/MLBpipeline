import requests
import json

def transform_games(games,transformed_teams):

    transformed_games = []

    teams_id = [team['id'] for team in transformed_teams]
    for date in games['dates']:
        for game in date['games']:
            if game['teams']['home']['team']['id'] in teams_id and game['teams']['away']['team']['id'] in teams_id:
                transformed_game = {
                'gameID': game['gamePk'],
                'gameDate': game['gameDate'],
                'status': game['status']['detailedState'],
                'homeTeamId': game['teams']['home']['team']['id'],
                'awayTeamId': game['teams']['away']['team']['id'],
                'homeScore': game['teams']['home'].get('score', 0),
                'awayScore': game['teams']['away'].get('score', 0),
                'venueId': game['venue']['id']
            
                }
                transformed_games.append(transformed_game)

    return transformed_games