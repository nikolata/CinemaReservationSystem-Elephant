CREATE_ADMINS = '''
    CREATE TABLE IF NOT EXISTS admins (
        admin_id INTEGER PRIMARY KEY NOT NULL,
        FOREIGN KEY (admin_id) REFERENCES users (id) ON DELETE CASCADE
    );
'''