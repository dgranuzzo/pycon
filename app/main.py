# -*- coding: utf-8 -*-
# https://fastapi.tiangolo.com/
import os
import uvicorn
from fastapi import FastAPI
from typing import Union
from models import Item

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/info")
def read_root():
    db_name = os.getenv('DB_NAME','no db')
    return {"db": db_name}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.post("/items/")
async def create_item(item: Item):
    return item


if __name__=='__main__':
    port=80
    print('listening on port {}'.format(port))
    uvicorn.run(app, host="0.0.0.0", port=port)