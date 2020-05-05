from .controller import UserContoller, AdminController


class UserViews:
    def __init__(self):
        self.controller = UserContoller()
        self.admin = AdminController()

    def login(self):
        pass

    def login_as_admin(self):
        username = input('Username: ')
        password = input('Password: ')

        self.admin.login(username=username, password=password)

    def signup(self):
        username = input('Username: ')
        password = input('Password: ')

        self.admin.create_admin(username=username, password=password)
