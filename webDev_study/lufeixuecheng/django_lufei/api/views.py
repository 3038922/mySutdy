from django.shortcuts import render, HttpResponse
# Create your views here.
from api import models


def test(request):
    # 插入VIP课程
    # obj1 = models.DegreeCourse.objects.filter(title='python全栈').first()
    # models.PricePolicy.objects.create(price=9.9, period=30, content_object=obj1)  #加个9.9 时间30天 加了GenericForeignKey('content_type', 'object_id') 就可以少写两个值

    # obj2 = models.DegreeCourse.objects.filter(title='python全栈').first()
    # models.PricePolicy.objects.create(price=19.9, period=60, content_object=obj2)

    # obj3 = models.DegreeCourse.objects.filter(title='python全栈').first()
    # models.PricePolicy.objects.create(price=29.9, period=90, content_object=obj3)

    # 插入普通课程 失败 提示django.db.utils.IntegrityError: (1048, "Column 'content_type_id' cannot be null")
    obj4 = models.DegreeCourse.objects.filter(title='rest_framework').first()
    models.PricePolicy.objects.create(price=9.9, period=30, content_object=obj4)  #加个9.9 时间30天 加了GenericForeignKey('content_type', 'object_id') 就可以少写两个值

    obj5 = models.DegreeCourse.objects.filter(title='rest_framework').first()
    models.PricePolicy.objects.create(price=19.9, period=60, content_object=obj5)

    obj6 = models.DegreeCourse.objects.filter(title='rest_framework').first()
    models.PricePolicy.objects.create(price=29.9, period=90, content_object=obj6)

    # 查询数据库
    # course = models.Course.objects.filter(id=1).first()
    # price_policys = course.price_policy_list.all()
    # print(price_policys)
    HttpResponse('....')
    # return Response('ok')
