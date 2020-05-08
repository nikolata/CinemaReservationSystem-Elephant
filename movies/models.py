class MovieModel:
    def __init__(self, id, name, rating):
        self.id = id
        self.name = name
        self.rating = rating

    def __str__(self):
        return f"[{self.id}] - {self.name} ({self.rating})"


class ProjectionModel:
    def __init__(self, id, movie_id, type, date, time):
        self.id = id
        self.movie_id = movie_id
        self.type = type
        self.date = date
        self.time = time


class ReservarionModel:
    def __init__(self, id, user_id, projection_id, row, col):
        self.id = id
        self.user_id = user_id
        self.projection_id = projection_id
        self.row = row
        self.col = col
