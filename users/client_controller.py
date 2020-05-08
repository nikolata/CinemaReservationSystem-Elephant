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
        self.client_gateway.add_to_table(user.id)
        self.login_client(username, password)
        return True

    def login_client(self, username, password):
        temp = self.client_gateway.login(username, password)
        if temp is False:
            return False
        settings.CURRENT_USER = temp
        return True

    def is_logged(self):
        return settings.CURRENT_USER != 0
