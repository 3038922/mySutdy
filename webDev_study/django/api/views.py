from rest_framework.response import Response  # DRF 返回类
from rest_framework.views import APIView  # DRF 视图类
from rest_framework.parsers import JSONParser  #DRF 导入JSON解析
from rest_framework import exceptions
from rest_framework.authentication import BasicAuthentication
from rest_framework.request import Request
from api import models
from api.utils.permission import MyPermission1  #单视图应用
ORDER_DICT = {1: {'name': '媳妇', 'age': 18, 'gender': '男', 'content': '详细信息'}, 2: {'name': '老狗', 'age': 8, 'gender': '女', 'content': '详细信息'}}


# 根据用户名生成MD5值
def md5(user):
    import hashlib
    import time
    ctime = str(time.time())  # 把当前时间转为字符串
    m = hashlib.md5(bytes(user, encoding='UTF-8'))  #第一层用户名MD5
    m.update(bytes(ctime, encoding='UTF-8'))  #加入时间戳
    return m.hexdigest()


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


class AuthView(APIView):
    """
    用于用户登录认证
    """
    authentication_classes = []  # 没登陆上不认证

    def get(self, request, *args, **kwargs):
        return Response('get ok')

    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        try:
            user = request.data.get('username')  #使用data 就可以解析json
            pwd = request.data.get('password')
            obj = models.UserInfo.objects.filter(username=user, password=pwd).first()
            print('POST请求DEBUG: ', user, ' ', pwd)
            #为登录用户创建索引
            token = md5(user)
            # 存在就更新 不存在就创建 token
            models.UserToken.objects.update_or_create(user=obj, defaults={'token': token})
            # 给用户返回token
            ret['token'] = token
        except Exception as e:
            print("e:", e)
            ret['code'] = 1002
            ret['msg'] = '请求异常'
        return Response(ret)


class OrderView(APIView):
    """
    订单相关业务(只有SVIP用户有权限)
    """

    # 权限控制 全局定义后默认都读全局的
    # permission_classes = [
    #     SVIPMyPermission,
    # ]

    def get(self, request, *args, **kwargs):
        # if request.user.user_type != 3:  # 权限控制
        #     return Response('无权访问')
        self.dispatch
        ret = {'code': 1000, 'msg': None, 'data': None}
        try:
            ret['data'] = ORDER_DICT
        except Exception as e:
            pass
        return Response(ret)

    def post(self, request, *args, **kwargs):
        pass


class UserInfoView(APIView):
    """
    订单相关业务
    """
    # 权限控制
    permission_classes = [
        MyPermission1,
    ]

    def get(self, request, *args, **kwargs):
        print(request.user)
        return Response('用户信息')


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
