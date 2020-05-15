from .client_model import ClientModel
from db import session
from .models import UserModel


class ClientGateway:
    # def add_to_table(self, user_id):
    #     query = ''' INSERT INTO clients(user_id)
    #                 VALUES (?);'''
    #     self.db.cursor.execute(query, (str(user_id),))
    #     self.db.connection.commit()

    #     query = f'''SELECT c.user_id, u.username, u.password, c.id
    #                 FROM clients c JOIN users u ON c.user_id = u.id
    #                 WHERE c.user_id = {user_id};'''
    #     self.db.cursor.execute(query)
    #     data = self.db.cursor.fetchall()
    #     return ClientModel(*data[0])

    def add_to_table(self, user_id):
        session.add(ClientModel(user_id=user_id))
        session.commit()
        client = session.query(ClientModel).filter(ClientModel.user_id == user_id).first()
        return client

    # def get_client_id(self, username, password):
    #     query = '''SELECT clients.id
    #                 FROM clients JOIN users ON clients.user_id = users.id
    #                 WHERE username = ? AND password = ?;'''
    #     self.db.cursor.execute(query, (username, hash_password(password)))

    #     client_id = self.db.cursor.fetchall()
    #     return client_id[0][0]

    def get_client_id(self, username):
        client_id = session.query(ClientModel.client_id).join(UserModel, ClientModel.user_id == UserModel.user_id).\
            filter(UserModel.name == username)
        return client_id[0]
