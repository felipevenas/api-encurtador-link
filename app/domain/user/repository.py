from sqlalchemy.orm import Session

from app.domain.user.model import User
from app.domain.user.schemas import ResponseUser, CreateUser

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: CreateUser) -> User:
        db_user = User(**user.model_dump())
        self.db.add(db_user)
        self.db.commit()
        return db_user