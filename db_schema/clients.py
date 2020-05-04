CREATE_CLIENTS = '''
    CREATE TABLE IF NOT EXISTS clients (
        client_id INTEGER PRIMARY KEY NOT NULL,
        FOREIGN KEY (client_id) REFERENCES users (id) ON DELETE CASCADE
    );
'''