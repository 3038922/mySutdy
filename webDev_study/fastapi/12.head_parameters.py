# -*- coding: utf-8 -*-
# 多参数

from fastapi import FastAPI, Header
from typing import List
app = FastAPI()


######################################################################
@app.get('/items/')
async def read_items(*, user_agent: str = Header(None), users_agent: str = Header(None)):
    """
    user_agent 永远返回系统的
    users_agent 这种改了下的 返回你实际输入的
    """
    return {"User_Agent": user_agent}, {"AAAAA": user_agent}, {"ABCD": users_agent}


######################################################################
@app.get('/items2/')
async def read_items2(x_token: List[str] = Header(None)):
    """
    x_token 命名不规范 会自动转成 x-token
    """
    return {"X-Token values": x_token}


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
