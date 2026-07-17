SELECT


    t.team_id,

    te.team_name,

    t.wins,

    t.losses,

    t.total_games,

    (t.wins + t.losses) AS calculated_games,

    t.home_wins + t.away_wins AS total_wins,

    t.home_losses + t.away_losses AS total_losses,

    Round((t.wins * 100.0 / t.total_games), 2) AS PCT_Wins,

    Round((t.losses * 100.0 / t.total_games), 2) AS PCT_losses

FROM team_season_records AS t
JOIN teams as te ON t.team_id = te.team_id 
ORDER BY t.wins DESC