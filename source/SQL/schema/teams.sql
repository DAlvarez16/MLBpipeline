CREATE TABLE Teams (

    team_id INT PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL,
    team_code VARCHAR(10) NOT NULL,
    location_name VARCHAR(100) NOT NULL,
    venue_id INTEGER NOT NULL,
    division_id INT NOT NULL,
    league_id INT NOT NULL,


    FOREIGN KEY (venue_id) REFERENCES venue(venue_id),
    Foreign Key (league_id) REFERENCES League(league_id),
    foreign key (division_id) references Division(division_id)

)