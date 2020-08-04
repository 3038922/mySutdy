# -*- coding: utf-8 -*-
"""
pip 不对
"""
from fastapi import FastAPI, Form, Request

app = FastAPI()

######################################################################


@app.post('/user/')
async def users(username: str = Form(...), password: str = Form(...)):
    return {"username": username, 'password': password}


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
