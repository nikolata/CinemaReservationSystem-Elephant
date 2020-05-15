from db import session
from .models import ProjectionModel
from sqlalchemy import and_


class ProjectionGateway:
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

    def select_all_for_given_date(self, movie_id, movie_date):
        return session.query(ProjectionModel).filter(
            and_(ProjectionModel.date == movie_date,
                 ProjectionModel.movie_id == movie_id)).order_by(ProjectionModel.time)

#     def select_all(self, movie_id):
#         query = f'''SELECT *
#                     FROM projections
#                     WHERE movie_id = {movie_id}
#                     ORDER BY date, time'''
#         self.db.cursor.execute(query)
#         projections = self.db.cursor.fetchall()
#         return [ProjectionModel(*data) for data in projections]

    def select_all(self, movie_id):
        return session.query(ProjectionModel).filter(ProjectionModel.movie_id == movie_id).\
            order_by(ProjectionModel.projection_date).order_by(ProjectionModel.projection_time)

#     def add_projection(self, movie_id, movie_type, date, time):
#         query = '''
#             INSERT INTO projections(movie_id, type, date, time)
#                 VALUES (?, ?, ?, ?)
#         '''
#         self.db.cursor.execute(query, (movie_id, movie_type, date, time))
#         self.db.connection.commit()

    def add_projection(self, movie_id, movie_type, date, time):
        session.add(ProjectionModel(movie_id=movie_id, projection_type=movie_type, projection_date=date,
                                    projection_time=time))
        session.commit()

#     def show_all_projections(self):
#         query = '''
#             SELECT * FROM projections
#         '''
#         self.db.cursor.execute(query)
#         projections = self.db.cursor.fetchall()
#         return [ProjectionModel(*projection) for projection in projections]

    def show_all_projections(self):
        projections = session.query(ProjectionModel).all()
        return projections
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

    def edit_projection(self, projection_id, new_id, new_type, new_date, new_time):
        session.query(ProjectionModel).filter(ProjectionModel.projection_id == projection_id).\
            update({ProjectionModel.movie_id: new_id,
                    ProjectionModel.projection_type: new_type,
                    ProjectionModel.projection_date: new_date,
                    ProjectionModel.projection_time: new_time}, synchronize_session=False)
        session.commit()

#     def delete_projection(self, projection_id):
#         query = '''
#             DELETE FROM projections
#             WHERE id = ?
#         '''
#         self.db.cursor.execute(query, (projection_id,))
#         self.db.connection.commit()

    def delete_projection(self, projection_id):
        projection = session.query(ProjectionModel).filter(ProjectionModel.projection_id == projection_id).first()
        session.delete(projection)

#     def select_one(self, projection_id):
#         self.db.cursor.execute(f'''SELECT *
#                                     FROM projections
#                                     WHERE id = {projection_id}''')
#         data = self.db.cursor.fetchall()
#         return ProjectionModel(*data[0])

    def select_one(self, projection_id):
        return session.query(ProjectionModel).filter(ProjectionModel.projection_id == projection_id).first()
