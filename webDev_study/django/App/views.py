from django.shortcuts import render
# 导入 HttpResponse
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, "index.html", context={"title": "Django", "name": "guguji"})
