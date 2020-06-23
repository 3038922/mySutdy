from django.urls import path
from django.urls import re_path
from App02 import views
# 路由列表 名称就叫 urlpatterns
app_name = "App02"  #应用的名空间 必须使用app_name 这个变量名字
urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/', views.handleAjax, name='ajax'),
]
