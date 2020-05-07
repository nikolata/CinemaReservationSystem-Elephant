from db import Database
from .models import MovieModel


class MovieGateway:
    def __init__(self):
        self.db = Database()
        self.movie = MovieModel

    def add_movie(self, name, rating):
        query = '''
            INSERT INTO movies(name, rating)
                VALUES (?, ?)
        '''

        self.db.cursor.execute(query, (name, rating))
        self.db.connection.commit()

    def show_all_movies(self):
        query = '''
            SELECT * FROM movies
        '''
        self.db.cursor.execute(query)
        movies = self.db.cursor.fetchall()
        return [MovieModel(*movie) for movie in movies]

    def get_all_movies_id(self):
        query = '''
            SELECT id FROM movies
        '''
        self.db.cursor.execute(query)
        movies_id = []
        movies = self.db.cursor.fetchall()
        for movie in movies:
            movies_id.append(movie[0])
        return movies_id

    def edit_movie(self, movie_id):
        query = '''
            SELECT name, rating FROM movies
            WHERE id == ?
        '''
        self.db.cursor.execute(query, (movie_id,))
        movie = self.db.cursor.fetchall()
        print(f'Old name {movie[0][0]}')
        new_movie_name = input(f'New name: ')
        print(f'Old rating {movie[0][1]}')
        new_movie_rating = input(f'New rating: ')
        update = '''
            UPDATE movies
            SET name = ?, rating = ?
            WHERE id == ?
        '''
        self.db.cursor.execute(update, (new_movie_name, new_movie_rating, movie_id))
        self.db.connection.commit()

    def delete_movie(self, movie_id):
        query = '''
        DELETE FROM movies
        WHERE id == ?
        '''
        self.db.cursor.execute(query, (movie_id,))
        query = '''
        DELETE FROM projections
        WHERE movie_id == ?
        '''
        self.db.cursor.execute(query, (movie_id,))
        self.db.connection.commit()
