from users.client_view import ClientView
from settings import ADMIN_PASSWORD


def welcome():
    print('Welcome to HackCinema!')
    command = int(input('Choose a command:\n  1 - log in\n  2 - sign up\n 3 - log in as admin\n Input: '))
    client_view = ClientView()

    if command == 1:
        return client_view.login()

    if command == 2:
        return client_view.signup()

    if command == 3:
        secret_password = input('Input the secret password: ')
        if secret_password == ADMIN_PASSWORD:
            return admin_views.login_as_admin()
        else:
            raise ValueError(f'Wrong password')

    raise ValueError(f'Unknown command {command}.')
