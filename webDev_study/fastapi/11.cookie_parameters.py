# -*- coding: utf-8 -*-
# 多参数

from fastapi import Cookie, FastAPI

app = FastAPI()


######################################################################
@app.get('/items/')
async def read_items(*, ads_id: str = Cookie(None)):
    return {"ads_id": ads_id}


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
