from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    path('users/', views.UsersList.as_view()),
    path('user/<int:pk>/', views.UsersDetail.as_view()),
]

# 对应不同请求头请求不同数据(Accept响应,Content-Type请求),json/html、form/json
urlpatterns = format_suffix_patterns(urlpatterns)
