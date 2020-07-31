# -*- coding: utf-8 -*-
from fastapi import FastAPI, status
app = FastAPI()

######################################################################


@app.post('/items/', status_code=201)
async def create_item(name: str):
    return {"name": name}


@app.get('/items2/', status_code=201)
async def create_item2(name: str):
    return {"name": name}


@app.post('/items3/', status_code=status.HTTP_404_NOT_FOUND)
async def create_item3(name: str):
    print('http_404:', status.HTTP_404_NOT_FOUND)
    return {"name": name}


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
