from fastapi import FastAPI

from app.domain.user.routes import user_router

app = FastAPI()

app.include_router(user_router)
