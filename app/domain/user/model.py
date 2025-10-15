from app.db.base_class import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(String(70), nullable=False)
    email = Column(String(100), nullable=False)
    login = Column(String(20), nullable=False)
    senha = Column(String(20), nullable=False)