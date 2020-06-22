from django.shortcuts import render
# 导入 HttpResponse
from django.http import HttpResponse
# Create your views here.
from App.models import User


def home(request):
    # 查询数据库
    users = User.objects.all()
    return render(request, "index.html", context={"title": "Django", "name": "挂机", "users": users})
