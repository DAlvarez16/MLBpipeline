def team_season_records(teams, games):
    records = {}

    for team in teams:
        records[team['id']] = {
            "team_id": team['id'],
            "wins": 0,
            "losses": 0,
            "home_wins":0,
            "away_wins":0,
            "home_losses":0,
            "away_losses":0,
            "total_games":0
        }
    for game in games:
             home = game["homeTeamId"]
             away = game["awayTeamId"]

             home_score = game["homeScore"]
             away_score = game["awayScore"]

             if game["status"] != "Final":
                continue

             records[home]['total_games'] += 1
             records[away]['total_games'] += 1

             if home_score > away_score:
                 records[home]['wins'] +=1
                 records[home]['home_wins'] +=1
                 records[away]['losses'] +=1
                 records[away]['away_losses'] +=1
             elif away_score > home_score:
                 records[home]['losses'] +=1
                 records[home]['home_losses'] +=1
                 records[away]['wins'] +=1
                 records[away]['away_wins'] +=1
    return list(records.values())