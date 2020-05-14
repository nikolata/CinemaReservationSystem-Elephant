from .controller import UserContoller
from .client_gateway import ClientGateway
import settings


class ClientController:
    def __init__(self):
        self.client_gateway = ClientGateway()
        self.controller = UserContoller()

    def create_client(self, username, password):
        user = self.controller.create_user(username, password)
        if not user:
            return False
        self.client_gateway.add_to_table(user.user_id)
        self.login_client(username, password)
        return True

    def login_client(self, username, password):
        settings.CURRENT_USER = self.client_gateway.get_client_id(username)[0]

    def is_logged(self):
        return settings.CURRENT_USER != 0
