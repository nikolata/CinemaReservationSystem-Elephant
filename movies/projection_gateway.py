from db import Database
from .models import ProjecttionModel


class ProjectionGateway:
    def __init__(self):
        self.db = Database()
        self.movie = ProjecttionModel

    def add_projection(self, movie_id, movie_type, date, time):
        query = '''
            INSERT INTO projections(movie_id, type, date, time)
                VALUES (?, ?, ?, ?)
        '''
        self.db.cursor.execute(query, (movie_id, movie_type, date, time))
        self.db.connection.commit()

    def show_all_projections(self):
        query = '''
            SELECT * FROM projections
        '''
        self.db.cursor.execute(query)
        projections = self.db.cursor.fetchall()
        return [ProjecttionModel(*projection) for projection in projections]

    def edit_projection(self, projection_id):
        query = '''
            SELECT movie_id, type, date, time FROM projections
            WHERE id == ?
        '''
        self.db.cursor.execute(query, (projection_id,))
        projection = self.db.cursor.fetchall()
        print(f'Old movie id: {projection[0][0]}')
        new_movie_id = input('New movie id: ')
        print(f'Old movie type: {projection[0][1]}')
        new_movie_type = input('New movie type: ')
        print(f'Old movie date: {projection[0][2]}')
        new_movie_date = input('New movie date: ')
        print(f'Old movie time: {projection[0][3]}')
        new_movie_time = input('New movie time: ')
        update = '''
        UPDATE projections
        SET movie_id = ?,
            type = ?,
            date = ?,
            time = ?
        WHERE id == ?
        '''
        self.db.cursor.execute(update, (new_movie_id, new_movie_type, new_movie_date, new_movie_time, projection_id))
        self.db.connection.commit()

    def delete_projection(self, projection_id):
        query = '''
            DELETE FROM projections
            WHERE id = ?
        '''
        self.db.cursor.execute(query, (projection_id,))
        self.db.connection.commit()
