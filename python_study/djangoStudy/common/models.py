from django.db import models

# Create your models here.


class Customer(models.Model):
    # 客户名称
    name = models.CharField(max_length=200)
    # 联系电话
    phonenumber = models.CharField(max_length=200)
    # 地址
    address = models.CharField(max_length=200)
    # QQ 新加入的条目的话 要加入缺省值 或允许为空值
    qq = models.CharField(max_length=30, null=True, blank=True)
