from db import Base
from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class ClientModel(Base):
    # def __init__(self, user_id, name, password, client_id):
    #     super().__init__(user_id, name, password)
    #     self.id = client_id

    __tablename__ = 'clients'

    client_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    user = relationship('UserModel')
