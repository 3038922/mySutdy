from django.conf.urls import url, include
from blog import views
from rest_framework import routers

app_name = 'JiaBlog'

# 定义路由地址
route = routers.DefaultRouter()

# 注册新的路由地址
route.register(r'getarticleinfo', views.GetArticleInfo)

urlpatterns = [
    url('api/', include(route.urls)),
]