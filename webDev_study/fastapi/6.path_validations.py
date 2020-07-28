# -*- coding: utf-8 -*-
# 路径验证
from fastapi import FastAPI, Path, Query  # Query查询参数的意思

app = FastAPI()


# http://127.0.0.1:11112/docs 测试
#  限制长度
@app.get('/items/{item_id}')
async def read_items(item_id: int = Path(..., title="The id of the item to get", ge=50, le=100),
                     q: str = Query(None, alias="item-query"),
                     size: float = Query(1, gt=0, lt=10.5)):
    """
    写None 选填 代表默认值是None
    写... 必填 代表没有东西
    ge 大于等于 le小于等于
    gt 大于 lt 小于
    """
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    return result


# 装饰器 @item_id
@app.get('/')
# async 异步的标识
async def main():
    return {'message': 'hellowrold,FastAPI'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=11112)

# uvicorn.exe .\1.hellowrold.py:app --reload
