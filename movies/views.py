from controller import MovieController, ProjectionController, ReservationController
from settings import CURRENT_USER


class MovieView:
    def __init__(self):
        self.controller = MovieController()

    def show_movies(self):
        movies = self.controller.show_movies()
        for i in movies:
            print(i)


class ProjectionView:
    def __init__(self):
        self.controller = ProjectionController()

    def show_projection(self, movie_id, movie_date=None):
        projection = self.controller.show_projection(movie_id, movie_date)
        for i in projection:
            print(i)


class ReservationView:
    def __init__(self):
        self.controller = ReservationController()

    def make_reservation(self):
        if CURRENT_USER == 0:
            print("You need to be a user in the system to make reservations!")
            #ToDo client login
        else:
            #ToDo 
            pass
