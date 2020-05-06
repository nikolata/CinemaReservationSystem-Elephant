from users.client_view import ClientView
from movies.views import ReservationView 
from users.views import UserViews, AdminViews
from settings import ADMIN_PASSWORD, CURRENT_USER


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
    admin_view = AdminViews()

    if command == 3:
        secret_password = input('Input the secret password: ')
        if secret_password == ADMIN_PASSWORD:
            return admin_views.login_as_admin()
        else:
            raise ValueError(f'Wrong password')

    raise ValueError(f'Unknown command {command}.')


def admin_options():
    command = int(input('''
        Choose a command:
        1 - show all admins
        2 - add admin
        3 - delete admin
        4 - add movie
        5 - add projection
        6 - show all movies
        7 - show all projections
        8 - edit movie
        9 - edit projection
        10 - delete projection
        11 - delete movie
        100 - exit
        Input: '''))
    admin_views = AdminViews()
    if command == 1:
        return admin_views.show_all_admins()
    if command == 2:
        return admin_views.add_admin()
    if command == 3:
        return admin_views.delete_admin()
    if command == 4:
        return admin_views.add_movie()
    if command == 5:
        return admin_views.add_projection()
    if command == 6:
        return admin_views.show_all_movies()
    if command == 7:
        return admin_views.show_all_projections()
    if command == 8:
        return admin_views.edit_movie()
    if command == 9:
        return admin_views.edit_projection()
    if command == 10:
        return admin_views.delete_projection()
    if command == 11:
        return admin_views.delete_movie()
    if command == 100:
        return 'Exit'
    raise ValueError('Error in admin_options')
