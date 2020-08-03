# -*- coding: utf-8 -*-
from fastapi import FastAPI, HTTPException, Request, JsonResponse
app = FastAPI()

######################################################################

items = {"foo", "the fook wrestlers"}


@app.get('/items/{item_id}')
async def read_item(item_id: str):
    """
    raise 用了以后 后面都不执行
    这么写前后端分离
    """
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    pass
    pass
    return {"item": items[item_id]}


######################################################################
@app.get('/items-header/{item_id}')
async def read_item_header(item_id: str):
    """
    raise 用了以后 后面都不执行
    这么写前后端分离
    添加自定义标题
    X-Error 自定义安全认证
    heards 不是header
    这里有问题
    """
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error "},
        )

    return {"item": items[item_id]}


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
