from django.shortcuts import render
# 导入 HttpResponse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse  # 反向代理
# Create your views here.
from App.models import Users

# 不使用模板引擎
# def index(request):
#     html = """"
#   <!DOCTYPE html>
#   <html lang="en">
#     <head>
#       <meta charset="UTF-8" />
#       <title>test</title>
#     </head>
#     <body>
#       <p>test!!!</p>
#     </body>
#   </html>"""
#     return HttpResponse(html)


# 使用模板引擎
def index(request):
    # 这个 渲染一次加载一次
    return render(request, "index.html", context=locals())


def handleAjax(request):
    if request.is_ajax():
        print("ajax")
        JsonResponse({'code': 0, 'msg': '登录成功'})
    else:
        print('not ajax')
    return render(request, "index.html")
    # return JsonResponse({'name': 'tom', 'age': 20})


# loader 加载一次 然后进行多次渲染
