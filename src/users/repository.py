from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.users.models import User  # ORM модель

class UserRepo:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_by_email(self, email: str) -> User | None:
        query = select(User).where(User.email == email)
        res = await self.session.execute(query)

        return res.scalar_one_or_none()


    async def add(self, user: User) -> User:
        self.session.add(user)
        return user
