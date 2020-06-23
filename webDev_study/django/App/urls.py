from django.urls import path
from App import views
# 路由列表 名称就叫 urlpatterns
urlpatterns = [
    # 不能/ 开头
    path('home/', views.home, name='home'),
    # 整数
    path('show/<int:age>/', views.show, name='show'),
    # 匹配由数字 字母、-和_组成的字符串参数
    path('list/<slug:name>/', views.listuser, name='listuser'),
    # path可以包含任何字符 包括/ 如果有多个参数 这个参数必须是最后一个
    path('access/<path:path>/', views.access, name='access')
]
