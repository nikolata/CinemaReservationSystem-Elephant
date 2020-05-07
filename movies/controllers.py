from .movie_gateway import MovieGateway
from .projection_gateway import ProjectionGateway
from .reservation_gateway import ReservationGateway
from settings import SPOTS_IN_ROW, SPOTS_IN_COL


class MovieController:
    def __init__(self):
        self.gateway = MovieGateway()

    def show_movies(self):
        return self.gateway.select_all()

    def get_name(self, id):
        return self.gateway.select_one(id).name


class ProjectionController:
    def __init__(self):
        self.gateway = ProjectionGateway()

    def show_projection(self, movie_id, movie_date):
        if movie_date:
            return self.gateway.select_all_for_all_for_given_date(movie_id, movie_date)
        else:
            return self.gateway.select_all(movie_id)

    def get_projection(self, projection_id):
        return self.gateway.select_one(projection_id)


class ReservationController:
    def __init__(self):
        self.gateway = ReservationGateway()

    def get_empty_spots(self, projection_id):
        return (SPOTS_IN_ROW * SPOTS_IN_COL)- self.gateway.get_reservations_count(projection_id)

    def generate_hall_places(self, projection_id):
        hall = [[False for col in range(SPOTS_IN_COL)] for row in range(SPOTS_IN_ROW)]
        taken_seats = self.gateway.get_row_and_col(projection_id)
        for row, col in taken_seats:
            hall[row - 1][col - 1] = True
        return hall

    def available_seat(self, projection_id, row, col):
        taken_seats = self.gateway.get_row_and_col(projection_id)
        return not((row, col) in taken_seats)

    def add_reservation(self, user_id, projection_id, row, col):
        self.gateway.add_reservation(user_id, projection_id, row, col)
