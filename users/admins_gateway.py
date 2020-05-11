from db import instance
from .models import AdminModel, UserModel
from .utls import hash_password


class AdminGateway:
    def __init__(self):
        self.model = AdminModel
        self.db = instance

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

    def show_all_admins(self, current_user):
        query = '''
        SELECT user_id, username, password FROM admins
        JOIN users ON admins.user_id = users.id
        '''
        self.db.cursor.execute(query)
        admins = self.db.cursor.fetchall()
        return [UserModel(*admin) for admin in admins]

    def delete_admin(self, number_id):
        delete_from_admin = '''
        DELETE FROM admins
        WHERE user_id == ?
        '''
        self.db.cursor.execute(delete_from_admin, (number_id,))
        delete_from_users = '''
        DELETE FROM users
        WHERE id == ?
        '''
        self.db.cursor.execute(delete_from_users, (number_id,))

        self.db.connection.commit()
        return number_id

    def get_admin_id(self, username, password):
        query = '''SELECT admins.id
                    FROM admins JOIN users ON admins.user_id = users.id
                    WHERE username = ? AND password = ?;'''
        self.db.cursor.execute(query, (username, hash_password(password)))
        admin_id = self.db.cursor.fetchall()
        return admin_id[0][0]
