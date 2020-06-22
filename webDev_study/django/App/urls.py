from django.urls import path
from App import views
# 路由列表 名称就叫 urlpatterns
urlpatterns = [
    # 不能/ 开头
    path('home/', views.home, name='home')
]
