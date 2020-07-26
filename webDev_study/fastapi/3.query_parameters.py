# -*- coding: utf-8 -*-
# 查询参数
from fastapi import FastAPI
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]  # 列表

app = FastAPI()


# http://127.0.0.1:11112/items/?skip=0&limit=2
@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip:skip + limit]


@app.get('/i/')
async def i(A: str = 'HI..', B: str = 'Hello..', C: str = 'He...'):
    return {"cc": A + B + C}, {'dd': B + C}


# http://127.0.0.1:11112/ii/?A=100
@app.get('/ii/')
async def ii(A: int = 0, B: int = 10, C: int = 20):
    return {"cc": A + B + C}, {'dd': B + C}


@app.get('/iii/')
async def iii(A: int = 0, B: int = 10, C: int = 20):
    return 'A+B+C', A + B + C


# http://127.0.0.1:11112/xxx/asdf?&QQ=316124534&SS=True
@app.get('/xxx/{item_id}')
async def xxx(item_id: str, QQ: str = None, SS: bool = False):
    item = {'item_id': item_id}
    if QQ:
        item.update({'QQ': QQ})
    if not SS:
        item.update({'item_id': "THIS is SSSSSSSSS"})
    return item


# http://127.0.0.1:11112/user/123/item/yyyyyyyyyy?q=%22qqqq%22&short=True
@app.get('/user/{user_id}/item/{item_id}')
async def read_user_item(user_id: int, item_id: str, q: str = None, short: bool = False):
    item = {'item_id': item_id, "owner_id": user_id}
    if q:
        item.update({'q': q})
    if not short:
        item.update({'description': 'This is  an amazing tiem that has a long description'})
    return item


# 装饰器 @
@app.get('/')
# async 异步的标识
async def main():
    return {'message': 'hellowrold,FastAPI'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=11112)

# uvicorn.exe .\1.hellowrold.py:app --reload