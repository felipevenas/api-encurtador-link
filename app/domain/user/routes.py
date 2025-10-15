from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.domain.user.repository import UserRepository
from app.domain.user.service import UserService
from app.domain.user.schemas import ResponseUser, CreateUser

user_router = APIRouter()

def get_user_service(db: Session = Depends(get_db)):
    repository = UserRepository(db)
    return UserService(repository)

@user_router.post("/register", response_model=ResponseUser)
def create(user: CreateUser, service: UserService = Depends(get_user_service)):
    return service.create(user)