SELECT
    t.team_name,
    s.wins,
    s.losses,
    s.home_wins,
    s.away_wins,
    s.home_losses,
    s.away_losses,
    s.total_games
FROM seasonrecords s
JOIN teams t
    ON s.team_id = t.team_id
ORDER BY s.wins DESC;