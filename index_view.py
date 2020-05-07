from users.client_view import ClientView
from settings import ADMIN_PASSWORD
from movies.views import ReservationView 

def welcome():
    print('Welcome to HackCinema!')
    command = int(input('Choose a command:\n  1 - log in\n  2 - sign up\n 3 - log in as admin\n Input: '))
    client_view = ClientView()

    if command == 1:
        client_view.login()
        client_view.commands()
        return

    if command == 2:
        client_view.signup()
        client_view.commands()
        return

    if command == 3:
        secret_password = input('Input the secret password: ')
        if secret_password == ADMIN_PASSWORD:
            return admin_views.login_as_admin()
        else:
            raise ValueError(f'Wrong password')

    raise ValueError(f'Unknown command {command}.')
