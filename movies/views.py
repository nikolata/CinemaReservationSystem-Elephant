from .controllers import MovieController, ProjectionController, ReservationController
from settings import CURRENT_USER, SPOTS_IN_ROW, SPOTS_IN_COL


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

    def show_projections(self, movie_id, movie_date=None, empty_spots = False):
        movie_controller = MovieController()
        movie_name = movie_controller.get_name(movie_id)
        projections = self.controller.show_projection(movie_id, movie_date)
        if movie_date:
            print(f"Projections for movie '{movie_name}' on date {movie_date}")
            for projection in projections:
                print(f"[{projection.id}] - {projection.time} ({projection.type})")
        else:
            print(f"Projections for movie '{movie_name}'")
            if empty_spots:
                reservation_controller = ReservationController()
                for projection in projections:
                    spots = reservation_controller.get_empty_spots(projection.id)
                    print((f"[{projection.id}] - {projection.date} {projection.time} ({projection.type}) - {spots} "
                                "spots available"))
            else:
                for projection in projections:
                    print(f"[{projection.id}] - {projection.date} {projection.time} ({projection.type})")


class ReservationView:
    def __init__(self):
        self.controller = ReservationController()

    def make_reservation(self):
        if CURRENT_USER == 0:
            print("You need to be a user in the system to make reservations!")
            #ToDo client login
        else:
            tickets = input('Step 1: Choose number of tikets: ')
            movie_view = MovieView()
            movie_view.show_movies()
            movie_id = input("Step 2: Choose movie id: ")
            projection_view = ProjectionView()
            projection_view.show_projections(movie_id=movie_id, empty_spots=True)
            projection_id = input("Step 3: Choose a projection id: ")
            hall_map = self.controller.generate_hall_places()
            row = " "
            for i in range(1, SPOTS_IN_COL + 1):
                row += f" {i}"
            print(row)
            hall_map = [['X' if seat else '.' for seat in row] for row in hall_map]
            for i in range(1,SPOTS_IN_ROW + 1):
                print(f"{i: <3}{" ".join(hall_map[i - 1])}")
            count = 1
            while tickets > 0:
                print(f"Step 4: Choose seat{count}: ")
                row = input("Choose row: ")
                col = input("Choose col: ")
                if self.controller.available_seat(projection_id, row, col):
                    tickets -= 1
                    count += 1
                    self.controller.add_reservation(CURRET_USER, projection_id, row, col)
                else:
                    print("It is taken!")
            
