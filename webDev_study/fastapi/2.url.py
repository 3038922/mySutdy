# -*- coding: utf-8 -*-
from fastapi import FastAPI
from enum import Enum


class Name(str, Enum):
    Allan = "张三"
    Jon = "李四"
    Bob = "王五"


app = FastAPI()


@app.get('/me/xx')
async def read_item_me():
    return {"me": "me"}


@app.get('/me/{item_id}')
async def read_item_me(item_id: str):
    return {"item_id": item_id}


# 装饰器 @
@app.get('/')
# async 异步的标识
async def main():
    return {'message': 'hellowrold,FastAPI'}


@app.get('/{who}')
async def get_day(who: Name):
    if who == Name.Allan:
        return {"who": who, "message": "法外狂徒张三"}
    if who.value == "李四":
        return {"who": who, "message": "被张三执法的李四"}
    return {"who": who, "message": "剩下的王五"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=11112)

# uvicorn.exe .\1.hellowrold.py:app --reload