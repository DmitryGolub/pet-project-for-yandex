import pytest

from src.users.models import User
from src.users.repository import UserRepo


@pytest.mark.anyio
async def test_user_repo_add_and_get_by_email(db_session):
    repo = UserRepo(db_session)

    user = User(
        email="a@b.com",
        username="alice",
        hashed_password="hash",
    )

    await repo.add(user)
    await db_session.commit()
    await db_session.refresh(user)

    got = await repo.get_by_email("a@b.com")
    assert got is not None
    assert got.id == user.id
    assert got.email == "a@b.com"
