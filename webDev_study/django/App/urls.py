from django.urls import path
from App import views
# 路由列表 名称就叫 urlpatterns
urlpatterns = [
    # 不能/ 开头
    path('home/', views.home, name='home'),
    # 整数
    path('show/<int:age>/', views.show, name='show'),
    # 匹配由数字 字母、-和_组成的字符串参数
    path('list/<slug:name>/', views.listuser, name='listuser')

]
