from .controller import AdminController


class AdminViews:
    def __init__(self):
        self.admin = AdminController()

    def login_as_admin(self):
        username = input('Username: ')
        password = input('Password: ')
        if self.admin.login(username=username, password=password) is True:
            return True
        return False

    def show_all_admins(self):
        self.admin.show_all_admins()

    def add_admin(self):
        temp_admin = AdminController()
        username = input('Username: ')
        password = input('Password: ')
        temp_admin.create_admin(username, password)

    def delete_admin(self):
        print('Please, choose which admin to delete (id number)')
        self.admin.show_all_admins()
        to_be_deleted_id = input('Input: ')
        self.admin.delete_admin(to_be_deleted_id)
