# -*- coding: utf-8 -*-
# 多参数
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field  # 数据验证模块 基础模式

app = FastAPI()


class Item(BaseModel):
    """
    JSON的OBJ格式
    没有给初始值的必填
    """
    name: str
    description: str = Field(None, title="description of the item", max_length=6)
    price: float = Field(..., gt=0, title="The price must be greater than zero")
    tax: float = None


class Item2(BaseModel):
    """
    JSON的OBJ格式
    没有给初始值的必填
    """
    name: str
    description: str = None
    price: float = Field(..., gt=0)
    tax: float = None


@app.put('/items/{item.id}')
async def update_item(*, item_id: int, item: Item = Body(..., embed=True)):
    """
    Body 的奇异值
    """
    result = {"item_id": item_id, "item": item}
    return result


@app.put('/items2/{item.id}')
async def update_item2(*,
                       item_id: int,
                       item: Item2 = Body(
                           ...,
                           example={
                               "name": "Foo",
                               "description": "A very nice Item",
                               "price": 0,
                               "toooo": 3.2,
                           })):
    """
    Body 的奇异值
    """
    result = {"item_id": item_id, "item": item}
    return result


# 装饰器 @item_id
@app.get('/')
# async 异步的标识
async def main():
    return {'message': 'hellowrold,FastAPI'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=11112)

# uvicorn.exe .\1.hellowrold.py:app --reload
