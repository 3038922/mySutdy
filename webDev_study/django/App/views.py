import json
from random import randint  # 使用randint需要加上这句
from django.core import serializers  #将查询结果转为JSON
# 导入 HttpResponse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse  # 反向代理

# Create your views here.
from App.models import TestMysql


def home(request):
    # 查询数据库
    users = TestMysql.objects.all()
    return render(request,
                  "index.html",
                  context={
                      "title": "Django",
                      "name": "挂机",
                      "users": users
                  })


# 视图函数第一个参数就是请求对象 由django传递
# 视图函数的作用 接受请求参数 调用模型模板 生成HTML字符串或者返回JSON数据  返回给客户端
# 至少知道GET POST FILES怎么获取


def show(request, name, age):
    print(type(age))
    return HttpResponse(name + ':' + str(age))


def listuser(request, name):
    print(name, type(name))
    return HttpResponse(name)


def access(request, path):
    return HttpResponse(path)


# GET请求测试


def getPhone(request, phone):
    # request对象常用属性
    # get请求传参的获取
    # 获取单一值 测试网址:http://10.195.106.43:8000/phone/15905706493/?username=3038922&age=18&age=23
    # queryDict=>dict
    print("得到请求的常规字典:", request.GET.dict())
    print(request.GET.get('username'))  # GET必须大写 获取到的是个字典 返回值是个对象
    # 获取多值
    print(request.GET.getlist('age'))  # GET必须大写 获取到的是个字典 多值返回值是个列表
    return HttpResponse(phone)


def getTel(request, tel):
    # 获取请求方式 是POST还是GET
    print(request.method)
    # 获取请求路径 返回/tel/15905706493/
    print(request.path)
    # 其他请求属性 返回一大堆
    # print(request.META)
    # 其他请求属性 客户端IP
    print('客户端IP:', request.META.get('REMOTE_ADDR'))
    # 来源页面 直接输入网址的返回NONE
    print('来源页面:', request.META.get('HTTP_REFERER'))
    print('相对路径:', request.get_full_path())
    print('主机HOST:', request.get_host())
    print('绝对路径:', request.build_absolute_uri())
    # POST请求测试
    print(request.POST.get('username'))
    print(request.POST.getlist('age'))
    return HttpResponse(tel)


def pathString(request, name):
    return HttpResponse(name)


def handleResponse(request):
    # res = HttpResponse("相应对象")
    # res.content_type = "text/html"
    # res.status_code = 400
    # return res
    # 只能处理字典 字典列表只能包含内置类型
    # return JsonResponse({'name': 'tom', 'age': 20})
    # 如果不是字典 必须  safe=False
    return JsonResponse([12121, 333, 44, 555], safe=False)


def handleRedirect(request):
    # 重定向到指定路由
    # return HttpResponseRedirect('/admin/')  # 重定向到首页
    # 快捷方式 等价于上面
    # return redirect('/admin/')
    # 也可以跳转百度
    # return redirect('https://www.baidu.com/')

    # 这个就是反向路由 由应用命令名空间:name来确定路由
    print(reverse('App:home'))  # 不带参数
    # 如果参数有名字 必须使用kwargs传参 如果没名字 比如正则 使用 args
    print(reverse('App:show', kwargs={'name': "chen", 'age': 20}))  # 带参数
    print(reverse('App:phone', args=('15905706493', )))  # 带参数 后面加个, 就正常了??

    return redirect(reverse('App:home'))


#反向定位:由应用的命名空间:name来确定路由


#增
def handleAdd(request):
    # user = TestMysql(username='admin121', password='protoss')
    # # 保存
    # user.save()

    # #便利方法 不需要save() 也可以创建循环来保存 效率低
    # user = {'username': 'adminaa22a', 'password': 'protoss'}
    # TestMysql.objects.create(**user)

    # 批量创建
    # TestMysql.objects.bulk_create([
    #     TestMysql(username='test1', password='protoss'),
    #     TestMysql(username='test2', password='protoss'),
    # ])
    # 模拟数据批量创建
    first = ["赵", "钱", "孙", "李", "周", "吴", "王"]
    lastname = ['三', '春花', '翠花', '卫国', '二狗']
    users = []
    for name in range(100):
        username = first[randint(0, 6)] + lastname[randint(0, 4)] + str(
            randint(0, 10000))
        users.append(
            TestMysql(username=username, password=str(randint(11111, 99999))))
    TestMysql.objects.bulk_create(users)
    return HttpResponse('增')


#删
def handleDelete(request):
    # 删除一条记录
    # try:
    #     user = TestMysql.objects.get(pk=1)  #pk 代表 uid
    #     print(user, type(user))
    #     if user:  #如果存在就删除
    #         user.delete()
    #     return HttpResponse('删')
    # except Exception as e:
    #     print(e)
    #     return HttpResponse('删除出错')
    # 删除多条记录
    users = TestMysql.objects.filter(uid__gte=5)  # 这表示UID大于等于5
    print(users)
    users.delete()
    return HttpResponse('批量删除')
    # 逻辑删除 就是假删除 数据库里不真删掉 大概就是回收站 增加一个字段 来判断


#改
def handleModify(request):
    #先查询
    user = TestMysql.objects.get(pk=1)  #pk 代表 uid
    #再修改
    user.password = "3333333"
    # 保存
    user.save()
    return HttpResponse('改')


# 查询 查询的返回类型都是QuerySet
def handleFindData(request):
    # all 过滤器 查询所有数据
    # data = TestMysql.objects.all()
    # filler 过滤器
    #data = TestMysql.objects.filter(uid=10)  #过滤uid等于10的
    # data = TestMysql.objects.filter(uid__gt=10)  #过滤uid大于10的
    # for it in data:
    #     print(it.username)

    # return HttpResponse(json.dumps(data))  #返回第一条结果

    # 查询结果转JSON
    data = {}
    res = TestMysql.objects.filter(uid__gt=10)
    data['result'] = json.loads(serializers.serialize('json', res))
    return JsonResponse(data)