# -*- coding: utf-8 -*-
# request 从客户端到服务器
# response 从服务器到客户端

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import List
app = FastAPI()

######################################################################


class Item(BaseModel):
    """
    JSON的OBJ格式
    没有给初始值的必填
    """
    name: str
    description: str = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


@app.post('/items/', response_model=Item)
async def create_item(item: Item):
    """
    response_model 关键字 响应模型 写地址后面
    """
    return item


######################################################################


class UserIn(BaseModel):
    """
    从客户端接收
    不要明文发送密码
    """
    name: str
    password: str
    email: EmailStr
    full_name: str = None


class UserOut(BaseModel):
    """
    发送给客户端
    """
    name: str
    email: EmailStr
    full_name: str = None


@app.post('/user/', response_model=UserOut)
async def create_user(*, user: UserIn):
    """
    response_model 关键字 响应模型 写地址后面
    最终要的功能是过滤和验证数据
    """
    return user


######################################################################
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


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    """
    * 是强制使用关键字
    item_id 填 boo bar baz
    根据字典的KEY 返回值
    response_model_exclude_unset 自定义JSON有的显示 没的就不显示 跟默认JSON无关
    """
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_publice_data(item_id: str):
    """
    * 是强制使用关键字
    item_id 填 boo bar baz
    response_model_exclude 排除关键字 比如排除tax选项 
    """
    return items[item_id]


@app.get("/items/{item_id}/name",
         response_model=Item,
         response_model_include={"name", "description", "tax"})
async def read_item_name(item_id: str):
    """
    * 是强制使用关键字
    item_id 填 boo bar baz
    response_model_include 包含关键字 比如包含"name", "description", "tax"选项 
    """
    return items[item_id]


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
