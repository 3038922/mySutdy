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

- 告诉 django 去 common 目录里看看,并更新数据库表 `python3 ./manage.py makemigrations common`

### lesson6

- 设置管理员账号密码 `python3 ./manage.py createsuperuser`
