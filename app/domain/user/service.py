from app.domain.user.repository import UserRepository
from app.domain.user.schemas import CreateUser, UpdateUser

class UserService():
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create(self, user: CreateUser):
        return self.repository.create(user)
    
    def get_by_id(self, id: int):
        return self.repository.get_by_id(id)
    
    def get_all(self):
        return self.repository.get_all()
    
    def delete(self, id: int):
        return self.repository.delete(id)
    
    def update(self, id: int, updated_user: UpdateUser):
        return self.repository.update(id, updated_user)