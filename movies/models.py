class MovieModel:
    def __init__(self, movie_id, name, rating):
        self.id = movie_id
        self.name = name
        self.rating = rating


class ProjecttionModel:
    def __init__(self, projection_id, movie_id, movie_type, date, time):
        self.id = projection_id
        self.movie_id = movie_id
        self.type = movie_type
        self.date = date
        self.time = time
