# from db import instance
# from .models import MovieModel


class MovieGateway:
    pass
#     def __init__(self):
#         self.db = instance

#     def select_all(self):
#         self.db.cursor.execute('''SELECT *
#                                     FROM movies
#                                     ORDER BY rating''')
#         movies = self.db.cursor.fetchall()
#         return [MovieModel(*data) for data in movies]

#     def select_one(self, id):
#         self.db.cursor.execute(f'''SELECT *
#                                     FROM movies
#                                     WHERE id = {id}''')
#         movie = self.db.cursor.fetchall()
#         return MovieModel(*movie[0])

#     def add_movie(self, name, rating):
#         query = '''
#             INSERT INTO movies(name, rating)
#                 VALUES (?, ?)
#         '''

#         self.db.cursor.execute(query, (name, rating))
#         self.db.connection.commit()

#     def get_all_movies_id(self):
#         query = '''
#             SELECT id FROM movies
#         '''
#         self.db.cursor.execute(query)
#         movies_id = []
#         movies = self.db.cursor.fetchall()
#         for movie in movies:
#             movies_id.append(movie[0])
#         return movies_id

#     def edit_movie(self, movie_id, new_movie_name, new_movie_rating):
#         update = '''
#             UPDATE movies
#             SET name = ?, rating = ?
#             WHERE id == ?
#         '''
#         self.db.cursor.execute(update, (new_movie_name, new_movie_rating, movie_id))
#         self.db.connection.commit()

#     def delete_movie(self, movie_id):
#         query = '''
#         DELETE FROM movies
#         WHERE id == ?
#         '''
#         self.db.cursor.execute(query, (movie_id,))
#         query = '''
#         DELETE FROM projections
#         WHERE movie_id == ?
#         '''
#         self.db.cursor.execute(query, (movie_id,))
#         self.db.connection.commit()

#     def get_movie_info(self, movie_id):
#         query = '''
#             SELECT * FROM movies
#             WHERE id == ?
#         '''
#         self.db.cursor.execute(query, (movie_id,))
#         movie = self.db.cursor.fetchall()
#         return MovieModel(movie[0][0], movie[0][1], movie[0][2])
