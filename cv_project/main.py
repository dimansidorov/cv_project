from fastapi import FastAPI

app = FastAPI(title='CV', debug=True)

@app.get('/')
async def hello_world():
    return {
        'data': 'hello world'
    }