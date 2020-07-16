from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Course(models.Model):
    """
    普通课程
    """
    title = models.CharField(max_length=32)
    # 仅用于反向查找
    price_policy_list = GenericRelation('PricePolicy')  # 查询数据库的组件


class DegreeCourse(models.Model):
    """
    学位课程
    """
    title = models.CharField(max_length=32)
    # 仅用于反向查找
    price_policy_list = GenericRelation('PricePolicy')  # 查询数据库的组件


class PricePolicy(models.Model):
    """
    价格策略
    """
    price = models.IntegerField()
    period = models.IntegerField()
    # table_name = models.CharField(verbose_name='关联的表名称')
    # object_id = models.CharField(verbose_name='关联的表中的数据行的ID')
    content_type = models.ForeignKey(ContentType, verbose_name='关键普通课或者学位课表', on_delete=models.CASCADE)
    object_id = models.IntegerField(verbose_name='关联的表中的数据行的ID')
    # 帮助你快速实现content_type操作
    content_object = GenericForeignKey('content_type', 'object_id')


# obj = DegreeCourse.objects.filter(title='python全栈').first()
# PricePolicy.objects.create(price=9.9, period=30, content_object=obj)  #加个9.9 时间30天 加了GenericForeignKey('content_type', 'object_id') 就可以少写两个值
"""
#1 为学位课'python全栈'添加一个价格策略 一个月9.9
obj = DegreeCourse.objects.filter(title='python全栈').first()
# obj.id
cobj = ContentType.objects.filter(model='course').first()
#cobj.id
PricePolicy.objects.create(price='9.9', period='30', content_type=cobj.id, object_id=obj.id)  #加个9.9 时间30天
"""