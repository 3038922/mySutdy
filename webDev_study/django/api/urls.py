from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^books/$', views.Book.as_view()),
    url(r'^books/(?P<pk>.*)/$', views.Book.as_view()),
    url(r'^v1/auth/$', views.AuthView.as_view()),
    url(r'^v1/order/$', views.OrderView.as_view()),
    url(r'^(?P<version>[v1|v2][v3]+)/userinfo/$', views.UserInfoView.as_view()),
    url(r'^(?P<version>[v1|v2][v3]+)/version/$', views.VersionView.as_view(), name='uuu'),
    url(r'^(?P<version>[v1|v2][v3]+)/parser/$', views.ParserView.as_view()),
    url(r'^(?P<version>[v1|v2][v3]+)/roles/$', views.RolesView.as_view()),
]
