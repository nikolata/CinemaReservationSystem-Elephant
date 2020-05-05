from db import Database
from .models import UserModel, AdminModel
from .utls import hash_password


class UserGateway:
    def __init__(self):
        self.model = UserModel
        self.db = Database()

    def create(self, *, username, password):
        self.model.validate(username, password)
        password = hash_password(password)
        query = '''
            INSERT INTO users (username, password)
                VALUES (?, ?)
        '''
        self.db.cursor.execute(query, (username, password))
        self.db.connection.commit()
        user_query = '''
            SELECT *
            FROM users
            ORDER BY id desc
            LIMIT 1
        '''
        self.db.cursor.execute(user_query)
        user_model = self.db.cursor.fetchall()
        self.model.id, self.model.name, self.model.password = user_model[0][0], user_model[0][1], user_model[0][2]
        return self.model

    def all(self):
        raw_users = self.db.cursor.execute()  # TODO: Select all users

        return [self.model(**row) for row in raw_users]


class AdminGateway:
    def __init__(self):
        self.model = AdminModel
        self.db = Database()

    def add_id_to_table(self, user_id):
        query = '''
            INSERT INTO admins (user_id)
                VALUES (?)
        '''
        self.db.cursor.execute(query, (user_id,))
        self.db.connection.commit()
        admin_query = '''
            SELECT id FROM admins
            ORDER BY id desc LIMIT 1
        '''

        self.db.cursor.execute(admin_query)
        admin_id = self.db.cursor.fetchall()

        return admin_id[0][0]

    def login(self, username, password):
        query = '''
            SELECT * FROM users
            WHERE username == ? and password == ?
        '''
        password = hash_password(password)
        self.db.cursor.execute(query, (username, password))
        user = self.db.cursor.fetchall()

        if len(user) == 0:
            answer = input('You dont have account yet. Do you want to create one? [y/n]: ')
            if answer == 'y':
                return 'create_account'
            else:
                return 'stop_the_program'
        safe_to_logged_in = '''
            INSERT INTO loggedin(user_id)
                VALUES (?)
        '''
        self.db.cursor.execute(safe_to_logged_in, (user[0][0],))
        self.db.connection.commit()
        self.model.user_id = user[0][0]
        return self.model

    def delete_from_loggedin(self, current_user):
        query = '''
        DELETE FROM loggedin
        WHERE user_id == ?
        '''
        self.db.cursor.execute(query, (current_user,))
        self.db.connection.commit()
