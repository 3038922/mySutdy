from django.urls import path
# 导入自己的写的函数
from sales.views import listorders, listcustomers
urlpatterns = [
    # 添加新的路由记录
    path('orders/', listorders),
    path('customers/', listcustomers),
]
