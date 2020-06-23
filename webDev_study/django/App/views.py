from django.shortcuts import render
# 导入 HttpResponse
from django.http import HttpResponse
# Create your views here.
from App.models import Users


def home(request):
    # 查询数据库
    users = Users.objects.all()
    return render(request, "index.html", context={"title": "Django", "name": "挂机", "users": users})


def show(request, age):
    print(type(age))
    return HttpResponse(str(age))


def listuser(request, name):
    print(name, type(name))
    return HttpResponse(name)


def access(request, path):
    return HttpResponse(path)


def getPhone(request, phone):
    return HttpResponse(phone)


def getTel(request, tel):
    return HttpResponse(tel)


def pathString(request, name):
    return HttpResponse(name)
