from .models import UserModel


class ClientModel(UserModel):
    def __init__(self, user_id, name, password, client_id):
        super().__init__(user_id, name, password)
        self.id = client_id
