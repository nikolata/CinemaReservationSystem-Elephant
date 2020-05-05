CREATE_PROJECTIONS = '''
    CREATE TABLE IF NOT EXISTS projections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_id INTEGER NOT NULL,
        type VARCHAR(10) NOT NULL,
        date DATE NOT NULL,
        time TIME NOT NULL,
        FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE
    );
'''
