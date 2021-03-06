from db import instance


class ReservationGateway:
    def __init__(self):
        self.db = instance

    def get_reservations_count(self, projection_id):
        self.db.cursor.execute(f'''SELECT COUNT(id)
                                    FROM reservations
                                    WHERE projection_id = {projection_id}''')
        return self.db.cursor.fetchall()[0][0]

    def get_row_and_col(self, projection_id):
        self.db.cursor.execute(f'''SELECT row, col
                                    FROM reservations
                                    WHERE projection_id = {projection_id}''')
        return self.db.cursor.fetchall()

    def add_reservation(self, user_id, projection_id, row, col):
        query = f'''INSERT INTO reservations (user_id, projection_id, row,col)
                    VALUES(?,?,?,?)'''
        self.db.cursor.execute(query, (user_id, projection_id, row, col))
        self.db.connection.commit()
