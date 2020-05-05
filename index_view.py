from users.views import UserViews
from settings import ADMIN_PASSWORD


def welcome():
    print('Welcome to HackCinema!')
    command = int(input('Choose a command:\n  1 - log in\n  2 - sign up\n 3 - log in as admin\n Input: '))
    user_views = UserViews()

    if command == 1:
        return user_views.login()

    if command == 2:
        return user_views.signup()

    if command == 3:
        secret_password = input('Input the secret password: ')
        if secret_password == ADMIN_PASSWORD:
            return user_views.login_as_admin()
        else:
            raise ValueError(f'Wrong password')

    raise ValueError(f'Unknown command {command}.')
