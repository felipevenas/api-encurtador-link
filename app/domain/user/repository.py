from sqlalchemy.orm import Session

from app.domain.user.model import User
from app.domain.user.schemas import CreateUser, UpdateUser

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: CreateUser) -> User:
        db_user = User(**user.model_dump())
        self.db.add(db_user)
        self.db.commit()
        return db_user

    def get_by_id(self, id: int) -> User:
        db_user = self.db.query(User).filter(User.id == id).first()
        if db_user:
            return db_user
        return None
    
    def get_all(self) -> list[User]:
        return self.db.query(User).all()
    
    def delete(self, id: int) -> User:
        db_user = self.db.query(User).filter(User.id == id).first()
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
            return db_user
        return None
    
    def update(self, id: int, updated_user: UpdateUser) -> User:
        db_user = self.db.query(User).filter(User.id == id).first()
        if db_user:
            db_user.nome = updated_user.nome
            db_user.email = updated_user.email
            db_user.login = updated_user.login
            self.db.commit()
            return db_user
        return None