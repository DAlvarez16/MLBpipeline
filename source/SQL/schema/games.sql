CREATE TABLE games  (
     gamesID INT PRIMARY KEY,
        gameDate TIMESTAMP NOT NULL,
        status VARCHAR(50) NOT NULL,
        homeTeamId INT NOT NULL,
        awayTeamId INT NOT NULL,
        homeTeamScore INT NOT NULL,
        awayTeamScore INT NOT NULL,
        venueid INT NOT NULL,

        foreign key (homeTeamId) references Teams(team_id),
        foreign key (awayTeamId) references Teams(team_id),
        foreign key (venueid) references Venue(venue_id)


)