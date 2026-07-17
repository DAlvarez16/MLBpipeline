SELECT

    team_id,

    wins,

    losses,

    total_games,

    (wins + losses) AS calculated_games,

    home_wins + away_wins AS total_wins,

    home_losses + away_losses AS total_losses

FROM team_season_records;