from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Course(models.Model):
    """
    普通课程
    """
    title = models.CharField(max_length=32)


class DegreeCourse(models.Model):
    """
    学位课程
    """
    title = models.CharField(max_length=32)


class PricePolicy(models.Model):
    """
    价格策略
    """
    price = models.IntegerField()
    period = models.IntegerField()
    # table_name = models.CharField(verbose_name='关联的表名称')
    # object_id = models.CharField(verbose_name='关联的表中的数据行的ID')
    content_type = models.ForeignKey(ContentType, verbose_name='关键普通课或者学位课表')
    object_id = models.IntegerField(verbose_name='关联的表中的数据行的ID')
