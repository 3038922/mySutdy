# -*- coding: utf-8 -*-
# 多参数
from fastapi import FastAPI, Path  # Query查询参数的意思
from pydantic import BaseModel  #数据验证模块 基础模式
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


@app.put('/items/{item.id}')
async def update_item(*,
                      item_id: int = Path(..., title="The id of the item to get", ge=0, le=1000),
                      q: str = None,
                      item: Item = None):
    """
    混合参数
    """
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    if Item:
        result.update({"item": item})
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
