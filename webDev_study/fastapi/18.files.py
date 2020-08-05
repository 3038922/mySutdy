# -*- coding: utf-8 -*-
from fastapi import FastAPI, File, UploadFile
from typing import List
app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    """
    字节形式
    """
    return {"file_size": len(file)}


######################################################################
@app.post("/uploadfile/")
async def create_upload_file(file: List[bytes] = File(...), fileb: UploadFile = File(...)):
    """
    上传形式
    fileb_content_type 判断类型
    """
    return {
        "file_size": len(file),
        "filebname": fileb.filename,
        "fileb_content_type": fileb.content_type
    }


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
