from fastapi import FastAPI
from stack.router import router as stack_router


app = FastAPI(title='CV', debug=True)


@app.get('/')
async def hello_world():
    return {
        'data': 'hello world'
    }


app.include_router(stack_router)