class UserModel:
    def __init__(self, *, user_id, name, password):
        self.id = user_id
        self.name = name
        self.password = password

    @staticmethod
    def validate(name, password):
        # TODO: Validate password to be ok -> Raise an error
        pass
    
    # @staticmethod
    # def login_required(func):
    #     def inner(*args, **kwargs):
    #         if user_id not in get_all_logged_ids():
    #             raise IndexError('YOU ARE NOT LOGGED IN')
    #         func(*args, **kwargs)
    #     return inner


class AdminModel:
    def __init__(self, *, admin_id):
        self.admin_id = admin_id

