from rest_framework import serializers  # rest_framework 的 序列化
from rest_framework import exceptions
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import \
    PageNumberPagination  # 用REST_FRAMEWORK自带类做分页
from rest_framework.parsers import FormParser  # DRF 导入JSON解析 导入FORM解析
from rest_framework.parsers import JSONParser
from rest_framework.request import Request  # 请求
from rest_framework.response import Response  # DRF 返回类
from rest_framework.views import APIView  # DRF 视图类
from rest_framework.viewsets import GenericViewSet, ModelViewSet  # 视图设置类
from api import models
from api.utils.permission import MyPermission1  # 单视图应用
from api.utils.serializsers.pager import PagerSerialiser  # 导入自己写的pagerxu'l
from api.utils.throttle import VisitThrottle  # 匿名用户登录限制

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
    permission_classes = []  # 这个名字不能乱取

    throttle_classes = [
        VisitThrottle,
    ]  # 匿名访问频率控制

    def get(self, request, *args, **kwargs):
        return Response('get ok')

    def post(self, request, *args, **kwargs):
        """
        1 去request 去获取IP 
        2 去做访问记录
        """
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


# class UserInfoSerializer(serializers.Serializer):
#     """
#     序列化方法1
#     """
#     user_type = serializers.IntegerField()  # 这样返回的是数组
#     ooo = serializers.CharField(source='get_user_type_display')  # 取用户组对应的中文
#     username = serializers.CharField()
#     password = serializers.CharField()
#     gp = serializers.CharField(source='group.title')
#     rls = serializers.SerializerMethodField()  # 自定义显示

#     def get_rls(self, row):
#         relo_obj_list = row.roles.all()
#         ret = []
#         for it in relo_obj_list:
#             ret.append({'id': it.id, 'tittle': it.title})
#         return ret

# class UserInfoSerializer(serializers.ModelSerializer):
#     """
#     序列化方法2
#     """
#     ooo = serializers.CharField(source='get_user_type_display')  # 取用户组对应的中文
#     rls = serializers.SerializerMethodField()  # 自定义显示

#     def get_rls(self, row):
#         relo_obj_list = row.roles.all()
#         ret = []
#         for it in relo_obj_list:
#             ret.append({'id': it.id, 'tittle': it.title})
#         return ret

#     class Meta:
#         model = models.UserInfo
#         # fields = '__all__'  #     这样写是获取全部数据库内容 但比较简陋
#         fields = ['ooo', 'id', 'username', 'password', 'rls']  # 实现上面一样的写法


class UserInfoSerializer(serializers.ModelSerializer):
    """
    序列化方法3 自动序列化链表
    """
    group = serializers.HyperlinkedIdentityField(view_name='gp', lookup_field='group_id', lookup_url_kwarg='pk')  # 这样写能反向出组的URL

    class Meta:
        model = models.UserInfo
        # fields = '__all__'  #     这样写是获取全部数据库内容 但比较简陋
        fields = ['id', 'username', 'password', 'group', 'roles']
        depth = 0  # 不写默认深度=0 0-10 一般写到3


class UserInfoView(APIView):
    """
    订单相关业务
    """
    # authentication_classes = []  # 没登陆上不认证
    # # 权限控制 谁都可以访问
    # permission_classes = [
    #     # MyPermission1,
    # ]
    throttle_classes = [
        VisitThrottle,
    ]  # 匿名访问频率控制

    def get(self, request, *args, **kwargs):
        users = models.UserInfo.objects.all()
        ser = UserInfoSerializer(instance=users, many=True, context={'request': request})
        # ret = json.dumps(ser.data, ensure_ascii=False)  # ensure_ascii=False 显示中文
        return Response(ser.data)  # 使用REST_FRAMEWORK 内置Response 就不用JSON解析一次了

    def post(self, request, *args, **kwargs):
        print(request.data)
        return Response('提交数据')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserGroup
        fields = '__all__'  #     这样写是获取全部数据库内容 但比较简陋


class GroupView(APIView):
    throttle_classes = [
        VisitThrottle,
    ]  # 匿名访问频率控制

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        obj = models.UserInfo.objects.filter(pk=pk).first()
        ser = GroupSerializer(instance=obj, many=False)
        # ret = json.dumps(ser.data, ensure_ascii=False)  # ensure_ascii=False 显示中文
        return Response(ser.data)


############################### 验证 ################################
class PasswordValidator(object):
    def __init__(self, base):
        self.base = base

    def __call__(self, value):
        if not value.startswith(self.base):
            message = '标题必须以 %s 开头.' % self.base
            raise serializers.ValidationError(message)

    def set_context(self, serializers_field):
        pass


class UserGroupSerializer(serializers.Serializer):
    title = serializers.CharField(error_messages={'required': '标题不能为空'}, validators=[PasswordValidator('老男人')])  # 不写可以

    class Meta:
        model = models.UserGroup
        fields = '__all__'  #     这样写是获取全部数据库内容 但比较简陋


class UserGroupView(APIView):
    throttle_classes = [
        VisitThrottle,
    ]  # 匿名访问频率控制

    def post(self, request, *args, **kwargs):
        print(request.data)
        ser = UserGroupSerializer(data=request.data)
        if ser.is_valid():
            print(ser.validated_data)
        else:
            print(ser.errors)
        return Response('提交数据')


###################################################################
class VersionView(APIView):
    """
    获取版本号
    """
    # 权限控制
    authentication_classes = []  # 没登陆上不认证
    permission_classes = [
        # MyPermission1,
    ]
    throttle_classes = [
        VisitThrottle,
    ]  # 匿名访问频率控制

    def get(self, request, *args, **kwargs):
        self.dispatch
        # print(request.user)
        print('版本号:', request.version)
        # 获取处理版本的对象
        print('获取处理版本的对象:', request.versioning_scheme)
        # 基于REST_FRAMEWORK  反向生成
        u1 = request.versioning_scheme.reverse(viewname='uuu', request=request)
        print('u1:', u1)
        # # 基于DJANGO 反向生成 不知道为啥不行
        # u2 = reverse(viewname='uuu', kwargs={'version': 3})
        # print('u2:', u2)
        return Response('获取版本号')


class ParserView(APIView):
    """
    解析
    """

    # 已设置为全局
    # parser_classes = [
    #     JSONParser,  # 只能解析 Content-type: application/json
    #     FormParser,  # 只能解析 `Content-type: application/x-www-form-urlencoded`
    # ]  #调用REST_FRAMEWORK 内置解析器 允许用户发JSON格式数据

    def get(self, request, *args, **kwargs):
        self.dispatch
        return Response('解析GET请求')

    def post(self, request, *args, **kwargs):
        self.dispatch  # ???这东西干嘛的 ?
        """
        1 获取用户请求
        2 获取用户请求体
        3 格局用户请求头 和   parser_classes = [JSONParser,FormParser] 中支持的请求头进行比较
        4 JSONParser || FormParser 对象去请求体
        5 request.data
        """
        print("request.data:", request.data)
        return Response('解析POST请求')


class RolesSerializer(serializers.Serializer):
    title = serializers.CharField()


class RolesView(APIView):
    throttle_classes = [
        VisitThrottle,
    ]  #

    # 权限控制
    def get(self, request, *args, **kwargs):
        # 方式1 但实际测试错误的 不知道为啥
        # roles = models.Role.objects.all().values('id', 'title')  # 拿到全部querySet
        # roles - list(roles)
        # ret = json.dumps(roles, ensure_ascii=False)  # ensure_ascii=False 显示中文
        # return HttpResponse(ret)
        # 方法2
        roles = models.Role.objects.all()
        ser = RolesSerializer(instance=roles, many=True)  # many=True 表示多条数据
        # ser.data 序列化后的结果 是个字典
        # ret = json.dumps(ser.data, ensure_ascii=False)  # ensure_ascii=False 显示中文
        return Response(ser.data)


class MyPageNumberPagination(PageNumberPagination):
    """
    继承写法
    """
    # 每页显示多少行
    page_size = 3
    # 配置页码 ?page=xxx用的
    page_query_param = 'page'
    # 传参数用
    page_size_query_param = None
    # 最大页面显示量
    max_page_size = None


class Pager1View(APIView):
    """
    分页
    """
    authentication_classes = []  # 没登陆上不认证
    # 权限控制 全局定义后默认都读全局的
    permission_classes = [
        # SVIPMyPermission,
    ]
    throttle_classes = [
        VisitThrottle,
    ]  #

    def get(self, request, *args, **kwargs):
        roles = models.Role.objects.all()
        # 创建分页对象
        # pg = PageNumberPagination() # 默认
        pg = MyPageNumberPagination()  # 自定义
        # 在数据库中获取分页数据
        pagerRoles = pg.paginate_queryset(queryset=roles, request=request, view=self)
        # 序列化分页后的数据
        ser = PagerSerialiser(instance=pagerRoles, many=True)
        # return Response(ser.data)  #用了Response 直接返回就是了 不用json了
        return pg.get_paginated_response(ser.data)  # 这样写多返回点东西 比如上一页 下一页


class V1View(GenericAPIView):
    """
    没啥用 GenericAPIView 继承了 APIView
    """
    # 权限控制 全局定义后默认都读全局的
    permission_classes = [
        # SVIPMyPermission,
    ]
    throttle_classes = [
        VisitThrottle,
    ]  #
    queryset = models.Role.objects.all()
    serializer_class = PagerSerialiser
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        # 获取数据
        roles = self.get_queryset()
        # 进行分页
        pager_roles = self.paginate_queryset(roles)
        # 序列化
        ser = self.get_serializer(instance=pager_roles, many=True)
        return Response(ser.data)


class V2View(GenericViewSet):
    """
    还是没啥用 GenericAPIView 继承了 APIView
    """
    # 权限控制 全局定义后默认都读全局的
    permission_classes = [
        # SVIPMyPermission,
    ]
    throttle_classes = [
        VisitThrottle,
    ]

    queryset = models.Role.objects.all()
    serializer_class = PagerSerialiser
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        # 获取数据
        roles = self.get_queryset()
        # 进行分页
        pager_roles = self.paginate_queryset(roles)
        # 序列化
        ser = self.get_serializer(instance=pager_roles, many=True)
        return Response(ser.data)


class V3View(ModelViewSet):
    """
    继承全能函数  增删改查都具备了
    复杂的 还是自己写吧
    通过改路由 可以确定自己需要的功能
    """
    # 权限控制 全局定义后默认都读全局的
    permission_classes = [
        # SVIPMyPermission,
    ]
    throttle_classes = [
        # VisitThrottle,
    ]

    queryset = models.Role.objects.all()
    serializer_class = PagerSerialiser
    pagination_class = PageNumberPagination

    # def list(self, request, *args, **kwargs):
    #     # 获取数据
    #     roles = self.get_queryset()
    #     # 进行分页
    #     pager_roles = self.paginate_queryset(roles)
    #     # 序列化
    #     ser = self.get_serializer(instance=pager_roles, many=True)
    #     return Response(ser.data)


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
