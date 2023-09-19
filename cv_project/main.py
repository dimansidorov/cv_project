from fastapi import FastAPI
from stack.router import router as stack_router
from auth.auth_config import auth_backend, fastapi_users
from auth.schemas import UserCreate, UserRead


app = FastAPI(title='CV', debug=True)


@app.get('/')
async def hello_world():
    return {
        'data': 'hello world'
    }


app.include_router(stack_router)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)