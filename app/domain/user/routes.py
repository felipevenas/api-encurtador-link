from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.domain.user.repository import UserRepository
from app.domain.user.service import UserService
from app.domain.user.schemas import ResponseUser, CreateUser, UpdateUser

user_router = APIRouter()

def get_user_service(db: Session = Depends(get_db)):
    repository = UserRepository(db)
    return UserService(repository)

@user_router.post("/register", response_model=ResponseUser)
def create(user: CreateUser, service: UserService = Depends(get_user_service)):
    user = service.create(user)
    return user

@user_router.get("/user/{id}", response_model=ResponseUser)
def get_by_id(id: int, service: UserService = Depends(get_user_service)):
    user = service.get_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")
    return user

@user_router.get("/users", response_model=list[ResponseUser])
def get_all(service: UserService = Depends(get_user_service)):
    users = service.get_all()
    if not users:
        raise HTTPException(status_code=404, detail="Usuários não encontrados!")
    return users

@user_router.delete("/user/{id}", response_model=ResponseUser)
def delete(id: int, service: UserService = Depends(get_user_service)):
    user = service.delete(id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")
    return user

@user_router.put("/user/{id}", response_model=ResponseUser)
def update(id: int, updated_user: UpdateUser, service: UserService = Depends(get_user_service)):
    user = service.update(id, updated_user)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")
    return user