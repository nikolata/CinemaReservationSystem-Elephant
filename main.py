import sys

from db import instance
from db_schema import (
    CREATE_USERS,
    CREATE_ADMINS,
    CREATE_CLIENTS,
    CREATE_MOVIES,
    CREATE_PROJECTIONS,
    CREATE_RESERVATIONS,
    CREATE_LOGGEDIN)

from index_view import welcome


class Application:
    @classmethod
    def build(self):
        db = instance
        db.cursor.execute(CREATE_USERS)
        db.cursor.execute(CREATE_CLIENTS)
        db.cursor.execute(CREATE_ADMINS)
        db.cursor.execute(CREATE_MOVIES)
        db.cursor.execute(CREATE_PROJECTIONS)
        db.cursor.execute(CREATE_RESERVATIONS)
        db.cursor.execute(CREATE_LOGGEDIN)
        # TODO: Seed with inistial data - consider using another command for this
        db.connection.commit()
        db.close()
        print('Done.')

    @classmethod
    def start(self):
        welcome()


if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'build':
        Application.build()
    elif command == 'start':
        Application.start()
        instance.close()
    else:
        instance.close()
        raise ValueError(f'Unknown command {command}. Valid ones are "build" and "start"')