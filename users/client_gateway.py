from db import Database
from .client_model import ClientModel
from .utls import hash_password


class ClientGateway:
    def __init__(self):
        self.model = ClientModel
        self.db = Database()

    def add_to_table(self, user_id):
        query = ''' INSERT INTO clients(user_id)
                    VALUES (?);'''
        self.db.cursor.execute(query, (str(user_id),))
        self.db.connection.commit()

        query = '''SELECT id
                    FROM clients
                    ORDER BY id DESC
                    LIMIT 1;'''
        self.db.cursor.execute(query)
        return self.model(self.db.cursor.fetchall()[0][0])

    def login(self, username, password):
        query = '''SELECT id
                    FROM users
                    WHERE username = ? AND password = ?;'''
        self.db.cursor.execute(query, (username, hash_password(password)))
        user_id = self.db.cursor.fetchall()
        if len(user_id) == 0:
            return False
        return user_id[0][0]
