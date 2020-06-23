from django.urls import path
from django.urls import re_path
from App import views
# 路由列表 名称就叫 urlpatterns
app_name = "App"  #应用的名空间 必须使用app_name 这个变量名字
urlpatterns = [
    # 不能/ 开头 path name 是命名路由的 跟路由无关
    path('home/', views.home, name='home'),
    # 整数
    path('show/<name>/<int:age>/', views.show, name='show'),
    # 匹配由数字 字母、-和_组成的字符串参数
    path('list/<slug:name>/', views.listuser, name='listuser'),
    # path可以包含任何字符 包括/ 如果有多个参数 这个参数必须是最后一个
    path('access/<path:path>/', views.access, name='access'),
    # path 普通string类型
    path('string/<name>/', views.pathString, name='strng'),

    # 正则写法 re_path 和path最大的区别就是政策模式串 手机号码匹配 写不出来只能写成匹配8个数字
    re_path(r'^phone/(\d{11})/$', views.getPhone, name='phone'),
    # 命名组 带参数的 参数必须叫tel
    re_path(r'^tel/(?P<tel>\d{11})/$', views.getTel, name='tel'),
    # 响应对象
    path('response/', views.handleResponse, name='response'),
    # 重定向
    path('red/', views.handleRedirect, name='response')
]
