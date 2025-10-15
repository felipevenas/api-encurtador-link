from app.domain.user.repository import UserRepository
from app.domain.user.schemas import CreateUser

class UserService():
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create(self, user: CreateUser):
        return self.repository.create(user)