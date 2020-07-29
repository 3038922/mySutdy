# -*- coding: utf-8 -*-
# 多参数
from typing import List, Set, Dict
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

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
    tags0: list = []
    tags1: List[str] = []
    tafs2: Set[str] = set()  # 生成一个集合必须这么写


@app.put('/items/{item.id}')
async def update_item(*, item_id: int, item: Item):
    """
    Body 的奇异值
    """
    result = {"item_id": item_id, "item": item}
    return result


######################################################################
class Image(BaseModel):
    url: str
    name: str


class Item2(BaseModel):
    """
    JSON的OBJ格式
    没有给初始值的必填
    """
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: Set[str] = set()  # 固定语法
    image: Image = None
    images: List[Image] = None


@app.put('/items2/{item.id}')
async def update_item2(*, item_id: int, item: Item):
    """
    Body 的奇异值
    """
    result = {"item_id": item_id, "item": item}
    return result


######################################################################


class Image(BaseModel):
    url: HttpUrl  # 该字符串将检查喂有效URL 并在JSON SCHEMA /OPENAPI 中进行记录
    name: str


@app.post('/images/multiple/')
async def create_multiple_images(*, images: List[Image]):
    """
    纯列标体
    """
    return images


@app.post('/index-weights/')
async def create_index_weights(weights: Dict[int, float]):
    """
    任意dicts 无需事先知道有效字段 属性名称是什么,如果你想接受未知密钥,这将很有用
    {
    "123": 0,
    "13": 0,
     "333": 0
    }
    """
    return weights


##########################################################################


# 装饰器 @item_id
@app.get('/')
# async 异步的标识
async def main():
    return {'message': 'hellowrold,FastAPI'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=11112)

# uvicorn.exe .\1.hellowrold.py:app --reload
