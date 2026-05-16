from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

@app.get('/items/{item_id}')
def read_item(item_id: int):
    return {'item_id': item_id, 'status': 'success'}