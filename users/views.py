from .client_controller import ClientController
from .controller import UserContoller, AdminController, AdminControllerInApp


class UserViews:
    def __init__(self):
        self.controller = UserContoller()
        self.admin = AdminController()

    def login(self):
        pass

    def login_as_admin(self):
        username = input('Username: ')
        password = input('Password: ')
        if self.admin.login(username=username, password=password) is True:
            return True
        return False

    def signup(self):
        username = input('Username: ')
        password = input('Password: ')

        self.admin.create_client(username=username, password=password)


class AdminViews:
    def __init__(self):
        self.admin = AdminControllerInApp()

    def show_all_admins(self):
        self.admin.show_all_admins()

    def add_admin(self):
        temp_admin = AdminControllerInApp()
        username = input('Username: ')
        password = input('Password: ')
        temp_admin.create_admin(username, password)

    def delete_admin(self):
        print('Please, choose which admin to delete (id number)')
        self.admin.show_all_admins()
        to_be_deleted_id = input('Input: ')
        self.admin.delete_admin(to_be_deleted_id)
