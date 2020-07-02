from django.http import JsonResponse
from django.views import View
from . import models


# Create your views here.
# 六大基础接口 获取一个 获取所有 增加一个 删除一个 整体更新一个 局部更新一个
# 十大接口 群增 群删 整体群改 局部改 群改
class Book(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:  # 群查
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
        return JsonResponse('post ok', safe=False)
