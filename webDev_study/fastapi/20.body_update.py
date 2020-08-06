# -*- coding: utf-8 -*-

from typing import List

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str = None
    description: str = None
    price: float = None
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {
        "name": "foo",
        "price": 50.2
    },
    "bar": {
        "name": "bar",
        "description": "the test2",
        "price": 62,
        "tax": 20.2
    },
    "baz": {
        "name": "baz",
        "description": None,
        "price": 50.2,
        "tax": 10.5,
        "tags": []
    }
}


######################################################################
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


######################################################################
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    """
    put 请求是更新功能
    """
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    print(items)
    return update_item_encoded


######################################################################
@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    """
    数据的局部更新
    比较麻烦 用的很少
    """
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)  # 必须写成True 不然就变成全部更新了
    print("update_data", update_data)
    updated_item = stored_item_model.copy(update=update_data)
    print('updated_item', updated_item)
    items[item_id] = jsonable_encoder(updated_item)
    print('items[item_id]', items[item_id])
    return updated_item


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
