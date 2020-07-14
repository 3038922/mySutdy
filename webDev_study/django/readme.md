# 我的 django 学习项目

## 基础命令

### lesson1

- 安装 django `pip3 install django`
- 查看版本 `python3.8 -m django --version`
- 创建新项目 `django-admin startproject djangoStudy`
- 启动服务 `python3.8 manage.py runserver 0.0.0.0:80`

### lesson2

- 创建应用项目 APP `python .\manage.py startapp sales`

### lesson4

- 创建 django 数据库所需要的一些表 `python3 ./manage.py migrate`
- 强制同步数据库表 `python3 manage.py migrate App --fake`

### lesson5

- 更新数据库表 `python3 ./manage.py makemigrations`
- 强制同步数据库表 `python3 manage.py migrate`
- 告诉 django 去 common 目录里看看,并更新数据库表 `python3 ./manage.py makemigrations common`

### lesson6

- 设置管理员账号密码 `python3 ./manage.py createsuperuser`

### DRF 框架 前后端分离仅做后端使用

- 安装框架 `pip3 install djangorestframework`

### django 声明周期

#### wsgi 协议

- wsgiref 是实现了 wsgi 协议的一个模块 模块本质 一个 socket 服务端 (django 框架)
- werkzeug 是实现了 wsgi 协议的一个模块 模块本质 一个 socket 服务端 (FLASK 框架)
- tornado 是实现了 wsgi 协议的一个模块 模块本质 一个 socket 服务端 (FLASK 框架)
- uwsgi 是实现了 wsgi 协议的一个模块 模块本质 一个 socket 服务端 (django 框架 线上使用 正式发布后使用)

### django 解析

- 请求头必须为 `Content-type: application/x-www-form-urlencoded` 时,`request.POST`中才会有值
- 数据格式要求: `name=alex&age=18&gender=男`
- ajax 提交 他会自动加上请求头 DATA 也会转变为 `name=alex&age=18&gender=男`

```
$.ajax{(
  usl:...,
  type:POST,
  data:{name:alex,age=18}
)}
```

- 情况 1:如果定制了请求头 requset.body 有值 request.POST 没有值

```
$.ajax{(
  usl:...,
  type:POST,
  headers:{'Content-type': "application/json"}
  data:{name:alex,age=18}
)}
```

- 情况 2:这样写依然 request.body 有值 request.POST 没有值

```
$.ajax{(
  usl:...,
  type:POST,
  headers:{'Content-type': "application/json"}
  data:JSON.stringfy({name:alex,age=18})
)}
```

- 如果是 JSON 传参
- 这样可以取到值 `json.loads(requset.boy)`

### rest framework 解析

- 使用`request.data`解析
- 视图函数加入`JSONParser`可以解析 JSON 但注意只能解析 `Content-type: application/json`
- 视图函数加入`FormParser`可以解析 form 但注意只能解析 `Content-type: application/x-www-form-urlencoded`

```
    parser_classes = [
        JSONParser,  # 只能解析 Content-type: application/json 这个头 其他头报错
    ]  #调用REST_FRAMEWORK 内置解析器 允许用户发JSON格式数据
```
