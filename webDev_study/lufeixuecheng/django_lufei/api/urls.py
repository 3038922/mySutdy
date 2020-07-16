from django.conf.urls import url, include
from api.views import test
from rest_framework import routers  # 使用rest_framework自带的自动路由

# router = routers.DefaultRouter()
# router.register(r'test', views.test)
urlpatterns = [
    url(r'test/$', test),
    # 加入自动路由
    # url(r'^(?P<version>[v1|v2|v3]+)/', include(router.urls)),
]