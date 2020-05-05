class UserModel:
    def __init__(self, *, user_id, name, password):
        self.id = user_id
        self.name = name
        self.password = password

    @staticmethod
    def validate(name, password):
        # TODO: Validate password to be ok -> Raise an error
        pass