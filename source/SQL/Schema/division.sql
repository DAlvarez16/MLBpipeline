CREATE Table Division (
    division_id INT PRIMARY KEY,
    division_name VARCHAR(100) NOT NULL,
    league_id INT NOT NULL,
    division_abbreviation VARCHAR(10) NOT NULL,
    

    foreign key (league_id) references League(league_id)
);