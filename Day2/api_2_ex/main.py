from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Hello, World!'}