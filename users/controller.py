from .users_gateway import UserGateway, AdminGateway


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

    def create_admin(self, username, password):
        controller = UserContoller()
        user = controller.create_user(username, password)
        admin = self.admin_gateway.add_id_to_table(user.id)

        self.current_user = admin

    def login(self, username, password):
        admin = self.admin_gateway.login(username, password)
        self.current_user = admin.user_id
        if self.current_user == 'create_account':
            username = input('Username: ')
            password = input('Password: ')
            self.create_admin(username, password)
        if self.current_user == 'stop_the_program':
            return

    def __del__(self):
        self.admin_gateway.delete_from_loggedin(self.current_user)
