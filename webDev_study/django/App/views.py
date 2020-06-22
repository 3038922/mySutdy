from django.shortcuts import render
# 导入 HttpResponse
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("hello wrold")
