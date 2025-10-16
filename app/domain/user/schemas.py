from pydantic import BaseModel

class ResponseUser(BaseModel):
    id: int
    nome: str
    email: str
    login: str
    senha: str

    class Config:
        from_attributes = True

class CreateUser(BaseModel):
    nome: str
    email: str
    login: str
    senha: str

class UpdateUser(BaseModel):
    nome: str
    email: str
    login: str