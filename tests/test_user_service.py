import pytest
from src.users.service import UserService


@pytest.mark.anyio
async def test_register_creates_user(db_session):
    service = UserService(db_session)

    user = await service.register(
        email="x@y.com",
        username="xuser",
        password="secret",
    )

    assert user.id is not None
    assert user.email == "x@y.com"
    assert user.username == "xuser"
    assert user.is_active is True
    assert user.created_at is not None
    assert user.updated_at is not None


@pytest.mark.anyio
async def test_register_duplicate_email_raises(db_session):
    service = UserService(db_session)

    await service.register(
        email="dup@y.com",
        username="u1",
        password="secret1",
    )

    with pytest.raises(ValueError, match="email already exists"):
        await service.register(
            email="dup@y.com",
            username="u2",
            password="secret2",
        )
