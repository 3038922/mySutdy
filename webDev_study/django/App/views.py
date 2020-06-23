from django.shortcuts import render
# 导入 HttpResponse
from django.http import HttpResponse
# Create your views here.
from App.models import Users


def home(request):
    # 查询数据库
    users = Users.objects.all()
    return render(request, "index.html", context={"title": "Django", "name": "挂机", "users": users})

# 视图函数第一个参数就是请求对象 由django传递
# 视图函数的作用 接受请求参数 调用模型模板 生成HTML字符串或者返回JSON数据  返回给客户端
# 至少知道GET POST FILES怎么获取


def show(request, age):
    print(type(age))
    return HttpResponse(str(age))


def listuser(request, name):
    print(name, type(name))
    return HttpResponse(name)


def access(request, path):
    return HttpResponse(path)

# GET请求测试


def getPhone(request, phone):
    # request对象常用属性
    # get请求传参的获取
    # 获取单一值 测试网址:http://10.195.106.43:8000/phone/15905706493/?username=3038922&age=18&age=23
    print(request.GET.get('username'))  # GET必须大写 获取到的是个字典 返回值是个对象
    # 获取多值
    print(request.GET.getlist('age'))  # GET必须大写 获取到的是个字典 多值返回值是个列表
    return HttpResponse(phone)

# POST请求测试


def getTel(request, tel):
    print(request.POST.get('username'))
    print(request.POST.getlist('age'))
    return HttpResponse(tel)


def pathString(request, name):
    return HttpResponse(name)
