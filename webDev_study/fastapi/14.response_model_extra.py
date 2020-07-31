# -*- coding: utf-8 -*-
# request 从客户端到服务器
# response 从服务器到客户端

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import List, Union, Dict
app = FastAPI()


##########################使用继承简化版################################
class UserBase(BaseModel):
    """
    基类
    """
    name: str
    email: EmailStr
    full_name: str = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    """
    加密
    """
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    """
    保存到数据库
    **user_in.dict() 数据验证的模块 大概相当于字典转JSON
    """
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)  #过滤掉PASSWORLD
    print("user_in_db:", user_in_db)
    print("User saved!..not readlly")
    return user_in_db


@app.post('/user/', response_model=UserOut)
async def create_user(*, user: UserIn):
    """
    response_model 关键字 响应模型 写地址后面
    最终要的功能是过滤和验证数据
    只返回改装过的用户数据 不带PASSWORLD
    """
    user_saved = fake_save_user(user)
    return user_saved


###############################Union##############################
class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type = "car"


class PlaneItem(BaseItem):
    type = "plane"
    size: int


items = {
    "item1": {
        "description": "All my friends drive a low rider",
        "type": "car"
    },
    "item2": {
        "description": "Musci is my aeroplane,it's my aeroplane",
        "type": "car",
        "size": 5
    }
}


@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    """
    * 是强制使用关键字
    item_id 填 boo bar baz
    根据字典的KEY 返回值
    Union[PlaneItem, CarItem] 联合起来 用后者覆盖前者
    """
    return items[item_id]


###############################List##############################
class Item(BaseModel):
    name: str
    description: str


items = [
    {
        "name": "Foo",
        "description": "There coms mu hero"
    },
    {
        "name": "Red",
        "description": "it's my aeroplane"
    },
]


@app.get("/items/", response_model=List[Item])
async def read_items():
    """
    LIST模型的格式 乱写报错
    """
    return items


###############################Dict##############################


@app.get("/keyword-weights/", response_model=Dict[str, float])
async def read_keyword_weights():
    """
    字典模型的格式 乱写报错
    """
    return {"foo": 2.3, "bar": 3.4}


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
