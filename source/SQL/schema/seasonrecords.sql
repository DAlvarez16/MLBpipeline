CREATE TABLE team_season_records (

    team_id INT PRIMARY KEY,
    wins INT NOT NULL,
    losses INT NOT NULL,
    home_wins INT NOT NULL,
    away_wins INT NOT NULL,
    home_losses INT NOT NULL,
    away_losses INT NOT NULL,
    total_games INT NOT NULL,

    FOREIGN KEY (team_id) REFERENCES teams(team_id)

);