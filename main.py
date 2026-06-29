import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fasthx.jinja import Jinja
from web import todo


app = FastAPI()
app.include_router(todo.router)

# Create a FastAPI Jinja2Templates instance and use it to create a
# FastHX Jinja instance that will serve as your decorator.
jinja = Jinja(Jinja2Templates("templates"))


@app.get('/')
@jinja.page('index.html')
async def index(request: Request):
    return {'todos': await todo.get_todos(), 'request': request}


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='127.0.0.1',
        port=8000,
        reload=True
    )
