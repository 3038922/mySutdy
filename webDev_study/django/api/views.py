from django.http import JsonResponse
from django.views import View
from . import models

from rest_framework.views import APIView  # DRF 视图类
from rest_framework.response import Response  # DRF 返回类


# Create your views here.
# 六大基础接口 获取一个 获取所有 增加一个 删除一个 整体更新一个 局部更新一个
# 十大接口 群增 群删 整体群改 局部改 群改
class Book(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:  # 群查
            # 序列化过程
            bookList = []
            for it in models.Book.objects.all():
                dic = {}
                dic['title'] = it.title
                dic['price'] = it.price
                bookList.append(dic)
            print("群查:", bookList)
            return JsonResponse({
                'status': 0,
                'msg': 'ok',
                'results': bookList
            },
                                json_dumps_params={'ensure_ascii': False})
        else:
            bookDic = models.Book.objects.filter(pk=pk).values(
                'title', 'price').first()
            if bookDic:
                return JsonResponse(
                    {
                        'status': 0,
                        'msg': 'ok',
                        'results': bookDic
                    },
                    json_dumps_params={'ensure_ascii': False})
            return JsonResponse({
                'status': 2,
                'msg': '无结果',
            },
                                json_dumps_params={'ensure_ascii': False})

    def post(self, request, *args, **kwargs):
        # 前台通过urlencoding 方式提交数据
        try:
            bookObj = models.Book.objects.create(**request.POST.dict())
            if bookObj:
                return JsonResponse(
                    {
                        'status': 0,
                        'msg': 'ok',
                        'results': bookObj
                    },
                    json_dumps_params={'ensure_ascii': False})
        except:
            return JsonResponse({
                'status': 1,
                'msg': '参数有误',
            },
                                json_dumps_params={'ensure_ascii': False})
        return JsonResponse({
            'status': 2,
            'msg': '新增失败',
        },
                            json_dumps_params={'ensure_ascii': False})
        print(request.body)
        return JsonResponse('post ok', safe=False)


# drf框架的封装风格


# from rest_framework.request import Request
# from rest_framework.serializers import Serializer
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated  # 是否登录用户
# from rest_framework.throttling import SimpleRateThrottle  # 频率
class Test(APIView):
    # 自定解析类
    def get(self, request, *args, **kwargs):
        return Response('drf ok')
