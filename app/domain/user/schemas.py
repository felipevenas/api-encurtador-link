from pydantic import BaseModel

class ResponseUser(BaseModel):
    id: int
    nome: str
    email: str
    login: str
    senha: str

class CreateUser(BaseModel):
    nome: str
    email: str
    login: str
    senha: str