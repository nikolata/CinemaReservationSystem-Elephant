from db import instance
from .models import ProjectionModel


class ProjectionGateway:
    def __init__(self):
        self.db = instance

    def select_all_for_given_date(self, movie_id, movie_date):
        query = f'''SELECT *
                    FROM projections
                    WHERE date = {movie_date} AND movie_id = {movie_id}
                    ORDER BY time'''
        self.db.cursor.execute(query)
        projections = self.db.cursor.fetchall()
        return [ProjectionModel(*data) for data in projections]

    def select_all(self, movie_id):
        query = f'''SELECT *
                    FROM projections
                    WHERE movie_id = {movie_id}
                    ORDER BY date, time'''
        self.db.cursor.execute(query)
        projections = self.db.cursor.fetchall()
        return [ProjectionModel(*data) for data in projections]
