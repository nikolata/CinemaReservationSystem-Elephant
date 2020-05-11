from db import instance
from .models import MovieModel


class MovieGateway:
    def __init__(self):
        self.db = instance

    def select_all(self):
        self.db.cursor.execute('''SELECT *
                                    FROM movies
                                    ORDER BY rating''')
        movies = self.db.cursor.fetchall()
        return [MovieModel(*data) for data in movies]

    def select_one(self, id):
        self.db.cursor.execute(f'''SELECT *
                                    FROM movies
                                    WHERE id = {id}''')
        movie = self.db.cursor.fetchall()
        return MovieModel(*movie[0])
