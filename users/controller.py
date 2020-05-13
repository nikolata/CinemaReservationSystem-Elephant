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

    def login(self, username, password):
        try:
            settings.CURRENT_USER = self.admin_gateway.get_admin_id(username, password)
        except Exception:
            return False
        return True

    def show_all_admins(self):
        return self.admin_gateway.show_all_admins()

    def create_admin(self, username, password):
        controller = UserContoller()
        user = controller.create_user(username, password)
        if not user:
            return False
        self.admin_gateway.add_id_to_table(user.id)
        self.login(username, password)

    def delete_admin(self, num_id):
        if num_id == settings.CURRENT_USER:
            raise TypeError('YOU CANT DELETE YOURSELF')
        return self.admin_gateway.delete_admin(num_id)
