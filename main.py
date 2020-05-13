import sys

from db import Base, engine
from index_view import login_start


class Application:
    @classmethod
    def build(self):
        Base.metadata.create_all(engine)
        print('Done.')

    @classmethod
    def start(self):
        login_start()


if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'build':
        Application.build()
    elif command == 'start':
        Application.start()
        # instance.close()
    else:
        # instance.close()
        raise ValueError(f'Unknown command {command}. Valid ones are "build" and "start"')
