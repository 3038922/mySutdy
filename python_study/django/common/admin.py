from django.contrib import admin

# Register your models here.

# 注册我们定义的model类
from .models import Customer

admin.site.register(Customer)
