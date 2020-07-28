# -*- coding: utf-8 -*-
# 多参数
from fastapi import FastAPI
from fastapi.param_functions import Body  # Query查询参数的意思
from pydantic import BaseModel  # 数据验证模块 基础模式

app = FastAPI()


class Item(BaseModel):
    """
    JSON的OBJ格式
    没有给初始值的必填
    """
    name: str
    description: str = None
    price: float
    tax: float = None


class User(BaseModel):
    username: str
    full_name: str = None


@app.put('/items/{item.id}')
async def update_item(*, item_id: int, item: Item, user: User, importance: int = Body(...)):
    """
    Body 的奇异值
    """
    result = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return result


@app.put('/items2/{item.id}')
async def update_item2(*, item_id: int, item: Item = Body(..., embed=True)):
    """
    embed=True 嵌入 False 不嵌入
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
