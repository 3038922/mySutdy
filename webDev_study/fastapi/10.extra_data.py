# -*- coding: utf-8 -*-
# 多参数
from datetime import datetime, time, timedelta
from uuid import UUID, uuid1
from pydantic import BaseModel
from fastapi import Body, FastAPI

app = FastAPI()


@app.put('/items/{item.id}')
async def read_item(item_id: UUID,
                    start_datetime: datetime = Body(None),
                    end_datetime: datetime = Body(None),
                    repeat_at: time = Body(None),
                    process_after: timedelta = Body(None)):
    """
    程序出错不知道为啥
    """
    start_proces = start_datetime + process_after
    duration = end_datetime - start_datetime
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": timedelta,
        "start_proces": start_proces,
        "duration": duration
    }


######################################################################
class Item(BaseModel):
    """
    JSON的OBJ格式
    没有给初始值的必填
    """
    start_datetime: datetime
    end_datetime: datetime
    repeat_at: time
    process_after: timedelta
    start_proces: str
    duration: str

    def calc(self):
        self.start_proces = self.start_datetime + self.process_after
        self.duration = self.end_datetime - self.start_datetime


@app.put('/items1/{item.id}')
async def read_items(item_id: UUID, item: Item):
    """
    上写报错 这边又对了...
    """
    item.start_proces = item.start_datetime + item.process_after
    item.duration = item.end_datetime - item.start_datetime
    # item.calc()
    return {"item_id": item_id, "item": item}


######################################################################


# 装饰器 @item_id
@app.get('/')
# async 异步的标识
async def main():
    return {'message': 'hellowrold,FastAPI'}


if __name__ == '__main__':
    import uvicorn
    print("uuid1:", uuid1())
    uvicorn.run(app, host='127.0.0.1', port=11112)

# uvicorn.exe .\1.hellowrold.py:app --reload
