from django.urls import include, path
from django.conf.urls import url, include
from api import views
from rest_framework import routers  # 自动路由
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),  # 自动路由
]