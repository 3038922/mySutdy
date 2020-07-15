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
    url(r'^(?P<version>[v1|v2][v3]+)/group/(?P<pk>\d+)$', views.GroupView.as_view(), name='gp'),  # 这样写能反向出组的URL
    url(r'^(?P<version>[v1|v2][v3]+)/usergroup/$', views.UserGroupView.as_view(), name='gp'),  # 提交数据
    url(r'^(?P<version>[v1|v2][v3]+)/pager1/$', views.Pager1View.as_view()),
]
