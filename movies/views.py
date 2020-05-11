from .controllers import MovieController, ProjectionController, ReservationController
from settings import SPOTS_IN_ROW, SPOTS_IN_COL
import settings
from users.client_controller import ClientController


class MovieView:
    def __init__(self):
        self.controller = MovieController()

    def show_movies(self):
        movies = self.controller.show_movies()
        for i in movies:
            print(i)

    def show_name(self, movie_id):
        print(self.controller.get_name(movie_id))


class ProjectionView:
    def __init__(self):
        self.controller = ProjectionController()

    def show_projections(self, movie_id, movie_date=None, empty_spots=False):
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

    def show_date(self, id):
        pass


class ReservationView:
    def __init__(self):
        self.controller = ReservationController()

    def make_reservation(self):
        client = ClientController()
        if not client.is_logged():
            print("You need to be a user in the system to make reservations!")
        else:
            tickets = int(input('Step 1: Choose number of tikets: '))
            movie_view = MovieView()
            movie_view.show_movies()
            movie_id = input("Step 2: Choose movie id: ")
            projection_view = ProjectionView()
            projection_view.show_projections(movie_id=movie_id, empty_spots=True)
            projection_id = input("Step 3: Choose a projection id: ")
            hall_map = self.controller.generate_hall_places(projection_id)
            row = " "
            for i in range(1, SPOTS_IN_COL + 1):
                row += f" {i}"
            print(row)
            hall_map = [['X' if seat else '.' for seat in row] for row in hall_map]
            for i in range(1, SPOTS_IN_ROW + 1):
                print(f"{i: <3}{' '.join(hall_map[i - 1])}")
            count = 1
            reserved_tickets = []
            while tickets > 0:
                print(f"Step 4: Choose seat {count}: ")
                row = input("Choose row: ")
                col = input("Choose col: ")
                if self.controller.available_seat(projection_id, row, col):
                    tickets -= 1
                    count += 1
                    self.controller.add_reservation(settings.CURRENT_USER, projection_id, row, col)
                    reserved_tickets.append((int(row), int(col)))
                else:
                    print("It is taken!")
            print("This is your reservation:")
            movie_controller = MovieController()
            movie_name = movie_controller.get_name(movie_id)
            print(f"Movie: {movie_name}")
            projection_controller = ProjectionController()
            projection = projection_controller.get_projection(projection_id)
            print(f"Date and time: {projection.date} {projection.time} ({projection.type}) ")
            print(f"Seats: {str(reserved_tickets).strip('[]')}")
