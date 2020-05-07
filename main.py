import sys

from db import Database
from db_schema import (
    CREATE_USERS,
    CREATE_ADMINS,
    CREATE_CLIENTS,
    CREATE_MOVIES,
    CREATE_PROJECTIONS,
    CREATE_RESERVATIONS,
    CREATE_LOGGEDIN)

from index_view import login_start  # welcome, admin_options


class Application:
    @classmethod
    def build(self):
        db = Database()
        db.cursor.execute(CREATE_USERS)
        db.cursor.execute(CREATE_CLIENTS)
        db.cursor.execute(CREATE_ADMINS)
        db.cursor.execute(CREATE_MOVIES)
        db.cursor.execute(CREATE_PROJECTIONS)
        db.cursor.execute(CREATE_RESERVATIONS)
        db.cursor.execute(CREATE_LOGGEDIN)
        # TODO: Seed with inistial data - consider using another command for this
        db.connection.commit()
        db.connection.close()

        print('Done.')

    @classmethod
    def start(self):
        # if welcome() is True:
        #     command = None
        #     while command is not 'Exit':
        #         command = admin_options()
        login_start()


if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'build':
        Application.build()
    elif command == 'start':
        Application.start()
    else:
        raise ValueError(f'Unknown command {command}. Valid ones are "build" and "start"')
