from django.views import View
from rest_framework.response import Response  # DRF 返回类
from rest_framework.views import APIView  # DRF 视图类
from rest_framework.parsers import JSONParser  #DRF 导入JSON解析
from . import models


class Book(APIView):
    # 局部配置解析
    parser_classes = [JSONParser]

    def get(self, request, *args, **kwargs):
        return Response('get ok')

    def post(self, request, *args, **kwargs):
        # url 拼接参数: 只有一种传参方式就是拼接参数
        print(request.query_params)
        # 数据包参数 有三种方式 form-data urlendcoding json
        print(request.data)
        return Response('post ok')


# Create your views here.
# 六大基础接口 获取一个 获取所有 增加一个 删除一个 整体更新一个 局部更新一个
# # 十大接口 群增 群删 整体群改 局部改 群改
# class Book(View):
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if not pk:  # 群查
#             # 序列化过程
#             bookList = []
#             for it in models.Book.objects.all():
#                 dic = {}
#                 dic['title'] = it.title
#                 dic['price'] = it.price
#                 bookList.append(dic)
#             print("群查:", bookList)
#             return JsonResponse({
#                 'status': 0,
#                 'msg': 'ok',
#                 'results': bookList
#             },
#                                 json_dumps_params={'ensure_ascii': False})
#         else:
#             bookDic = models.Book.objects.filter(pk=pk).values(
#                 'title', 'price').first()
#             if bookDic:
#                 return JsonResponse(
#                     {
#                         'status': 0,
#                         'msg': 'ok',
#                         'results': bookDic
#                     },
#                     json_dumps_params={'ensure_ascii': False})
#             return JsonResponse({
#                 'status': 2,
#                 'msg': '无结果',
#             },
#                                 json_dumps_params={'ensure_ascii': False})

#     def post(self, request, *args, **kwargs):
#         # 前台通过urlencoding 方式提交数据
#         try:
#             bookObj = models.Book.objects.create(**request.POST.dict())
#             if bookObj:
#                 return JsonResponse(
#                     {
#                         'status': 0,
#                         'msg': 'ok',
#                         'results': bookObj
#                     },
#                     json_dumps_params={'ensure_ascii': False})
#         except:
#             return JsonResponse({
#                 'status': 1,
#                 'msg': '参数有误',
#             },
#                                 json_dumps_params={'ensure_ascii': False})
#         return JsonResponse({
#             'status': 2,
#             'msg': '新增失败',
#         },
#                             json_dumps_params={'ensure_ascii': False})
#         print(request.body)
#         return JsonResponse('post ok', safe=False)

# drf框架的封装风格

# from rest_framework.request import Request
# from rest_framework.serializers import Serializer
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated  # 是否登录用户
# from rest_framework.throttling import SimpleRateThrottle  # 频率
# drf 对原生request做了二次封装 requestl._request 就是原生request
# 原生request 对象和睡醒和方法都可以被drf兼容
