from sqlalchemy.ext.asyncio import AsyncSession
from src.users.models import User
from src.users.repository import UserRepo
from src.users.security import hash_password


class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repo = UserRepo(session)

    async def register(self, email: str, username: str, password: str) -> User:
        existing = await self.repo.get_by_email(email)
        if existing:
            raise ValueError("email already exists")

        user = User(
            email=email,
            username=username,
            hashed_password=hash_password(password),
        )
        await self.repo.add(user)

        try:
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise

        await self.session.refresh(user)
        return user
