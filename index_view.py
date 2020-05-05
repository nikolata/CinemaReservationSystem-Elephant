from users.views import AdminViews
from settings import ADMIN_PASSWORD, CURRENT_USER


def welcome():
    print('Welcome to HackCinema!')
    command = int(input('Choose a command:\n  1 - log in\n  2 - sign up\n 3 - log in as admin\n Input: '))
    admin_view = AdminViews()

    # if command == 1:
    #     return user_views.login()

    # if command == 2:
    #     return user_views.signup()

    if command == 3:
        secret_password = input('Input the secret password: ')
        if secret_password == ADMIN_PASSWORD:
            return admin_view.login_as_admin()
        else:
            raise ValueError(f'Wrong password')

    raise ValueError(f'Unknown command {command}.')


def admin_options():
    command = int(input('Choose a command:\n1 - show all admins\n 2 - add admin\n 3 - delete admin\n4 - exit\nInput:'))
    admin_views = AdminViews()
    if command == 1:
        return admin_views.show_all_admins()
    if command == 2:
        return admin_views.add_admin()
    if command == 3:
        return admin_views.delete_admin()
    if command == 4:
        return 'Exit'
    raise ValueError('Error in admin_options')
