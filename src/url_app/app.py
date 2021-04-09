from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import router


app = FastAPI()
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
)


@app.get('/')
def root():
    return {'hello': 'world'}
