from .controller import MovieController, ProjectionController


class MovieViews:
    def __init__(self):
        self.movie = MovieController()

    def add_movie(self):
        name = input('Movie name: ')
        rating = input('Rating: ')
        self.movie.add_movie(name, rating)

    def show_all_movies(self):
        self.movie.show_all_movies()

    def edit_movie(self):
        movie_id = input('Movie id: ')
        self.movie.edit_movie(movie_id)

    def delete_movie(self):
        movie_id = input('Movie id: ')
        self.movie.delete_movie(movie_id)


class ProjectionViews:
    def __init__(self):
        self.projection = ProjectionController()

    def add_projection(self):
        temp = MovieViews()
        temp.show_all_movies()
        movie_id = input('Movie id: ')
        movie_type = input('Movie type: ')
        date = input('Date: ')
        time = input('Time: ')
        self.projection.add_projection(int(movie_id), movie_type, date, time)

    def show_all_projections(self):
        self.projection.show_all_projections()

    def edit_projection(self):
        projection_id = input('Projection id: ')
        self.projection.edit_projection(projection_id)

    def delete_projection(self):
        projection_id = input('Projection id: ')
        self.projection.delete_projection(projection_id)
