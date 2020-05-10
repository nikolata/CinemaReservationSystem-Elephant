from .client_controller import ClientController
from getpass import getpass
import re
from movies.views import MovieView, ProjectionView, ReservationView


class ClientView:
    def __init__(self):
        self.controller = ClientController()
        self.movie_view = MovieView()
        self.reservaion_view = ReservationView()
        self.projection_view = ProjectionView()
        self.date_pattern = re.compile(r'^\d\d\d\d-\d\d-\d\d$')

    def login(self):
        username = input('Username: ')
        password = input('Password: ')

        self.controller.login_client(username, password)

    def signup(self):
        incorrect_password = True
        username = input('Username: ')
        while incorrect_password:
            password = getpass()
            password_comfirm = getpass('Enter passoword again: ')
            if password == password_comfirm:
                incorrect_password = False
            else:
                print("Comfirmation failed")

        return self.controller.create_client(username=username, password=password)

    def command_2(self):
        print('You have to enter movie id')
        print("If you dont't know the id press 0 and you will see the id for all the movies")
        movie_id = int(input('Enter id: '))
        if movie_id == 0:
            self.movie_view.show_movies()
            self.command_2()
        else:
            print('You can enter a date.In format: year-month-day.')
            print("If you don't want to enter date press 0")
            incorrect_date = True
            while incorrect_date:
                movie_date = input("Enter date: ")
                if movie_date == '0':
                    self.projection_view.show_projections(movie_id)
                    incorrect_date = False
                else:
                    if self.date_pattern.match(movie_date):
                        self.projection_view.show_projections(movie_id, )
                        incorrect_date = False
                    else:
                        print('Incorrect date')

    def commands(self):
        print('You can choose from: ')
        print('1. show movies')
        print('2. show movie projections')
        print('3. make reservation')
        command = int(input('Enter: '))
        if command == 1:
            self.movie_view.show_movies()
        if command == 2:
            self.command_2()
        if command == 3:
            self.reservaion_view.make_reservation()
        else:
            print("Not a valid command!")
            self.commands()
