from .controllers import MovieController, ProjectionController, ReservationController
from settings import CURRENT_USER, SPOTS_IN_ROW, SPOTS_IN_COL
from users.client_controller import ClientController


class MovieView:
    def __init__(self):
        self.movie = MovieController()

    def show_movies(self):
        movies = self.movie.show_movies()
        for i in movies:
            print(i)

    def add_movie(self):
        name = input('Movie name: ')
        rating = input('Rating: ')
        self.movie.add_movie(name, rating)

    def show_all_movies(self):
        movies = self.movie.show_movies()
        for movie in movies:
            print(f'{movie.id} | {movie.name} | {movie.rating}')

    def edit_movie(self):
        movie_id = input('Movie id: ')
        self.movie.edit_movie(movie_id)

    def delete_movie(self):
        movie_id = input('Movie id: ')
        self.movie.delete_movie(movie_id)


class ProjectionView:
    def __init__(self):
        self.projection = ProjectionController()

    def show_projections(self, movie_id, movie_date=None, empty_spots=False):
        movie_controller = MovieController()
        movie_name = movie_controller.get_name(movie_id)
        projections = self.projection.show_projection(movie_id, movie_date)
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

    def add_projection(self):
        temp = MovieView()
        temp.show_all_movies()
        movie_id = input('Movie id: ')
        movie_type = input('Movie type: ')
        date = input('Date: ')
        time = input('Time: ')
        self.projection.add_projection(int(movie_id), movie_type, date, time)

    def show_all_projections(self):
        projections = self.projection.show_all_projections()
        for projection in projections:
            print(f'{projection.id} | {projection.movie_id} | {projection.type} | {projection.date} |'
                  f'{projection.time}')

    def edit_projection(self):
        projection_id = input('Projection id: ')
        self.projection.edit_projection(projection_id)

    def delete_projection(self):
        projection_id = input('Projection id: ')
        self.projection.delete_projection(projection_id)


class ReservationView:
    def __init__(self):
        self.controller = ReservationController()

    def make_reservation(self):
        client = ClientController()
        if not client.is_logged():
            print("You need to be a user in the system to make reservations!")
            # ToDo client login
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
            while tickets > 0:
                print(f"Step 4: Choose seat{count}: ")
                row = input("Choose row: ")
                col = input("Choose col: ")
                if self.controller.available_seat(projection_id, row, col):
                    tickets -= 1
                    count += 1
                    self.controller.add_reservation(CURRENT_USER, projection_id, row, col)
                else:
                    print("It is taken!")


# class MovieViews:
#     def __init__(self):
#         self.movie = MovieController()

#     def add_movie(self):
#         name = input('Movie name: ')
#         rating = input('Rating: ')
#         self.movie.add_movie(name, rating)

#     def show_all_movies(self):
#         movies = self.movie.show_all_movies()
#         for movie in movies:
#             print(f'{movie.id} | {movie.name} | {movie.rating}')

#     def edit_movie(self):
#         movie_id = input('Movie id: ')
#         self.movie.edit_movie(movie_id)

#     def delete_movie(self):
#         movie_id = input('Movie id: ')
#         self.movie.delete_movie(movie_id)


# class ProjectionViews:
#     def __init__(self):
#         self.projection = ProjectionController()

#     def add_projection(self):
#         temp = MovieViews()
#         temp.show_all_movies()
#         movie_id = input('Movie id: ')
#         movie_type = input('Movie type: ')
#         date = input('Date: ')
#         time = input('Time: ')
#         self.projection.add_projection(int(movie_id), movie_type, date, time)

#     def show_all_projections(self):
#         projections = self.projection.show_all_projections()
#         for projection in projections:
#             print(f'{projection.id} | {projection.movie_id} | {projection.type} | {projection.date} |'
#                   f'{projection.time}')

#     def edit_projection(self):
#         projection_id = input('Projection id: ')
#         self.projection.edit_projection(projection_id)

#     def delete_projection(self):
#         projection_id = input('Projection id: ')
#         self.projection.delete_projection(projection_id)
