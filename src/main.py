from fastapi import FastAPI

from src.auth.router import router as auth_router
from src.users.router import router as user_router

app = FastAPI()


app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/users", tags=["users"])
