# -*- coding: utf-8 -*-
# 查询参数
from fastapi import FastAPI
from pydantic import BaseModel  #数据验证模块 基础模式


class Item(BaseModel):
    """
    JSON的OBJ格式
    没有给初始值的必填
    """
    name: str
    description: str = None
    price: float
    tax: float = None


app = FastAPI()


# http://127.0.0.1:11112/docs 测试
@app.post('/items')
async def create_item(item: Item):
    print(item.dict())
    return item, '人生没有无意义的经历.'


@app.put('/items/{item.id}')
async def create_item2(item_id: int, item: Item, q: str = None):
    result = {"item_id:": item_id, **item.dict()}  # **item.dict() 似乎是罗列字典
    if q:
        result.update({"q", q})
    print(result)
    return result


# 装饰器 @
@app.get('/')
# async 异步的标识
async def main():
    return {'message': 'hellowrold,FastAPI'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=11112)

# uvicorn.exe .\1.hellowrold.py:app --reload
