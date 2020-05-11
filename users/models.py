class UserModel:
    def __init__(self, user_id, name, password):
        self.id = user_id
        self.name = name
        self.password = password

    @staticmethod
    def validate(name, password):
        if len(password) < 8:
            return False
        if any(letter.isupper() for letter in password) < 1:
            return False
        special_symbols = ['>', '<', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '.', ',']
        if len([letter for letter in password if letter in special_symbols]) < 1:
            return False
        return True

    # @staticmethod
    # def login_required(func):
    #     def inner(*args, **kwargs):
    #         if user_id not in get_all_logged_ids():
    #             raise IndexError('YOU ARE NOT LOGGED IN')
    #         func(*args, **kwargs)
    #     return inner


class AdminModel(UserModel):
    def __init__(self, admin_id, user_id, name, password):
        super().__init__(user_id, name, password)
        self.admin_id = admin_id
