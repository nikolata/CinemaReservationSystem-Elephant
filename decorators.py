# from db import instance
from db import session


def atomic(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        # session.commit()
        # query = 'BEGIN TRANSACTION;'
        # instance.cursor.execute(query)
        # try:
        #     func(*args, **kwargs)
        #     instance.connection.commit()
        # except Exception as exc:
        #     print(exc)
        #     instance.cursor.execute('''ROLLBACK;''')
    return inner


def login_required(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)

        # if settings.CURRENT_USER == 0:
        #     print('You have to log first')
        # else:
        #     func(*args, **kwargs)
    return inner
