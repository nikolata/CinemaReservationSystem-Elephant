import unittest
from unittest.mock import MagicMock
from users.client_gateway import ClientGateway
from users.users_gateway import UserGateway
from users.models import UserModel
from users.client_controller import ClientController
import settings


class TestClientController(unittest.TestCase):
    def test_if_user_is_none_creat_returns_false(self):
        gateway = UserGateway()
        gateway.create = MagicMock(return_value=None)
        c_controller = ClientController()
        c_controller.controller.users_gateway = gateway
        name = 'fa'
        password = 'asdfghjkA@'

        self.assertFalse(c_controller.create_client(name, password))

    def test_if_client_is_logged_when_created(self):
        gateway = UserGateway()
        name = 'fa'
        password = 'asdfghjkA@'
        model = UserModel(1, name, password)
        gateway.create = MagicMock(return_value=model)
        c_controller = ClientController()
        c_controller.controller.users_gateway = gateway
        c_gateway = ClientGateway()
        c_controller.client_gateway = c_gateway
        c_gateway.add_to_table = MagicMock(return_value=1)
        c_gateway.login = MagicMock(return_value=1)

        self.assertTrue(c_controller.create_client(name, password))
        self.assertTrue(settings.CURRENT_USER == 1)


if __name__ == '__main__':
    unittest.main()
