from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^books/$', views.Book.as_view()),
    url(r'^books/(?P<pk>.*)/$', views.Book.as_view()),
    url(r'^v1/auth/$', views.AuthView.as_view()),
    url(r'^v1/order/$', views.OrderView.as_view()),
]
