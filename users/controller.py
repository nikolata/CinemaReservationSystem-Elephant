from .users_gateway import UserGateway
from .admins_gateway import AdminGateway
import settings


class UserContoller:
    def __init__(self):
        self.users_gateway = UserGateway()

    def create_user(self, username, password):
        user = self.users_gateway.create(username=username, password=password)
        return user
        # send email
        # sync with Slack


class AdminController:
    def __init__(self):
        self.admin_gateway = AdminGateway()
        self.current_user = None

    def login(self, username, password):
        admin = self.admin_gateway.login(username, password)
        curr_user = admin.user_id
        if curr_user == 'create_account':
            username = input('Username: ')
            password = input('Password: ')
            self.create_admin(username, password)
        if curr_user == 'stop_the_program':
            return False
        settings.CURRENT_USER = curr_user
        return True


class AdminControllerInApp:
    def __init__(self):
        self.admin_gateway = AdminGateway()

    def show_all_admins(self):
        self.admin_gateway.show_all_admins(settings.CURRENT_USER)

    def create_admin(self, username, password):
        controller = UserContoller()
        user = controller.create_user(username, password)
        self.admin_gateway.add_id_to_table(user.id)

    def delete_admin(self, num_id):
        self.admin_gateway.delete_admin(num_id)
