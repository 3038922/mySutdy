# 导入 HttpResponse
from django.shortcuts import redirect, render

# from django.urls import reverse  # 反向代理
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# from App.models import Users

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

# # 使用模板引擎
# def index(request):
#     # 这个 渲染一次加载一次
#     return render(request, "index.html", context=locals())

# def handleAjax(request):
#     if request.is_ajax():
#         print("ajax请求", request)
#         JsonResponse({'code': 0, 'msg': '登录成功'})
#     else:
#         print('not ajax')
#     return render(request, "index.html")
#     # return JsonResponse({'name': 'tom', 'age': 20})


# 注册
# 局部禁止 csrf检测
# @csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("用户名:", username, "密码:", password)
    else:
        print("不是AJAX POST请求")
    return render(request, "index.html")
