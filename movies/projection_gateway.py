# from db import instance
# from .models import ProjectionModel


class ProjectionGateway:
    pass
#     def __init__(self):
#         self.db = instance

#     def select_all_for_given_date(self, movie_id, movie_date):
#         query = f'''SELECT *
#                     FROM projections
#                     WHERE date = {movie_date} AND movie_id = {movie_id}
#                     ORDER BY time'''
#         self.db.cursor.execute(query)
#         projections = self.db.cursor.fetchall()
#         return [ProjectionModel(*data) for data in projections]

#     def select_all(self, movie_id):
#         query = f'''SELECT *
#                     FROM projections
#                     WHERE movie_id = {movie_id}
#                     ORDER BY date, time'''
#         self.db.cursor.execute(query)
#         projections = self.db.cursor.fetchall()
#         return [ProjectionModel(*data) for data in projections]

#     def add_projection(self, movie_id, movie_type, date, time):
#         query = '''
#             INSERT INTO projections(movie_id, type, date, time)
#                 VALUES (?, ?, ?, ?)
#         '''
#         self.db.cursor.execute(query, (movie_id, movie_type, date, time))
#         self.db.connection.commit()

#     def show_all_projections(self):
#         query = '''
#             SELECT * FROM projections
#         '''
#         self.db.cursor.execute(query)
#         projections = self.db.cursor.fetchall()
#         return [ProjectionModel(*projection) for projection in projections]

#     def edit_projection(self, projection_id, new_id, new_type, new_date, new_time):
#         query = '''
#             SELECT movie_id, type, date, time FROM projections
#             WHERE id == ?
#         '''
#         self.db.cursor.execute(query, (projection_id,))
#         projection = self.db.cursor.fetchall()
#         update = '''
#         UPDATE projections
#         SET movie_id = ?,
#             type = ?,
#             date = ?,
#             time = ?
#         WHERE id == ?
#         '''
#         self.db.cursor.execute(update, (new_id, new_type, new_date, new_time, projection_id))
#         self.db.connection.commit()

#     def delete_projection(self, projection_id):
#         query = '''
#             DELETE FROM projections
#             WHERE id = ?
#         '''
#         self.db.cursor.execute(query, (projection_id,))
#         self.db.connection.commit()

#     def select_one(self, projection_id):
#         self.db.cursor.execute(f'''SELECT *
#                                     FROM projections
#                                     WHERE id = {projection_id}''')
#         data = self.db.cursor.fetchall()
#         return ProjectionModel(*data[0])
