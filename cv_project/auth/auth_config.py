import uuid

from fastapi_users.authentication import CookieTransport, AuthenticationBackend, JWTStrategy
from fastapi_users import FastAPIUsers
from config import COOKIE_LIFETIME, SECRET_KEY, JWT_LIFETIME

from .models import User
from .manager import get_user_manager


cookie_transport = CookieTransport(cookie_max_age=COOKIE_LIFETIME)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_KEY, lifetime_seconds=JWT_LIFETIME)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)


fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)