from db import session
from .models import AdminModel, UserModel


class AdminGateway:
    # def add_id_to_table(self, user_id):
    #     query = '''
    #         INSERT INTO admins (user_id)
    #             VALUES (?)
    #     '''
    #     self.db.cursor.execute(query, (user_id,))
    #     self.db.connection.commit()
    #     admin_query = '''
    #         SELECT id FROM admins
    #         ORDER BY id desc LIMIT 1
    #     '''

    #     self.db.cursor.execute(admin_query)
    #     admin_id = self.db.cursor.fetchall()

    #     return admin_id[0][0]

    def add_id_to_table(self, user_id):
        session.add(AdminModel(user_id=user_id))
        a_id = session.query(AdminModel.admin_id).filter(AdminModel.user_id == user_id).first()
        session.commit()
        return a_id[0]

    # def show_all_admins(self, current_user):
    #     query = '''
    #     SELECT user_id, username, password FROM admins
    #     JOIN users ON admins.user_id = users.id
    #     '''
    #     self.db.cursor.execute(query)
    #     admins = self.db.cursor.fetchall()
    #     return [UserModel(*admin) for admin in admins]

    def show_all_admins(self):
        admins = session.query(AdminModel).all()
        return admins

    # def delete_admin(self, number_id):
    #     delete_from_admin = '''
    #     DELETE FROM admins
    #     WHERE user_id == ?
    #     '''
    #     self.db.cursor.execute(delete_from_admin, (number_id,))
    #     delete_from_users = '''
    #     DELETE FROM users
    #     WHERE id == ?
    #     '''
    #     self.db.cursor.execute(delete_from_users, (number_id,))

    #     self.db.connection.commit()
    #     return number_id

    def delete_admin(self, number_id):
        to_be_deleted = session.query(AdminModel).filter(AdminModel.admin_id == number_id).first()
        to_be_deleted_user = session.query(UserModel).filter(UserModel.user_id == to_be_deleted.user_id).first()
        session.delete(to_be_deleted)
        session.delete(to_be_deleted_user)
        session.commit()
        return number_id

    # def get_admin_id(self, username, password):
    #     query = '''SELECT admins.id
    #                 FROM admins JOIN users ON admins.user_id = users.id
    #                 WHERE username = ? AND password = ?;'''
    #     self.db.cursor.execute(query, (username, hash_password(password)))
    #     admin_id = self.db.cursor.fetchall()
    #     return admin_id[0][0]

    def get_admin_id(self, username, password):
        ad_id = session.query(AdminModel.admin_id).join(UserModel).filter(UserModel.name == username)
        return ad_id[0]
