# -*- coding: utf-8 -*-
"""
转换成 json
"""
from datetime import *

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str = None


app = FastAPI()


######################################################################
@app.put('/items/{id}')
async def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    print(json_compatible_item_data)
    print(type(json_compatible_item_data))
    print(fake_db)
    print(type(fake_db))


# return {"file_size": len(file)}


######################################################################
# 装饰器 @item_id
@app.get('/')
# async 异步的标识
async def main():
    return {'message': 'hellowrold,FastAPI'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=11112)

# uvicorn.exe .\1.hellowrold.py:app --reload
