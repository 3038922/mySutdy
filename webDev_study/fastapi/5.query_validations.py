# -*- coding: utf-8 -*-
# 参数验证
from fastapi import FastAPI, Query  # Query查询参数的意思
from typing import List  # 列表

app = FastAPI()


# http://127.0.0.1:11112/docs 测试
#  限制长度
@app.get('/items/')
async def read_items(q: str = Query(None, min_length=3, max_length=50)):
    """
    写None 选填 代表默认值是None
    写... 必填 代表没有东西
    """
    result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result


#正则表达式
@app.get('/items2/')
async def read_items2(q: str = Query(..., min_length=3, max_length=50, regex="^nice")):
    """
    写None 选填 代表默认值是None
    写... 必填 代表没有东西
    必须以nice开头
    """
    result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result


#列表 可以自由添加参数
@app.get('/items3/')
async def read_items3(q: List[str] = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items


#别名参数 http://127.0.0.1:11112/items4/?item-query=sdafdasff
#用item-query替换q
@app.get('/items4/')
async def read_items4(q: str = Query(..., alias="item-query")):
    """
    写None 选填 代表默认值是None
    写... 必填 代表没有东西
    """
    result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result


# 弃用参数
@app.get('/items5/')
async def read_items5(q: str = Query(None,
                                     alias="item-query",
                                     title="Query string",
                                     description="一大堆字符串",
                                     min_length=3,
                                     max_length=50,
                                     regex="^fixedquery$",
                                     deprecated=True)):
    """
    写None 选填 代表默认值是None
    写... 必填 代表没有东西
    deprecated=True 代表整个弃用
    """
    result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result


# 装饰器 @
@app.get('/')
# async 异步的标识
async def main():
    return {'message': 'hellowrold,FastAPI'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=11112)

# uvicorn.exe .\1.hellowrold.py:app --reload
