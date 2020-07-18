from django.contrib import admin
from django.urls import include
from django.conf.urls import url
from django.urls import path
from django.conf import settings
from backEnd_django.settings import MEDIA_ROOT
from django.conf.urls.static import static
from blog import views
from haystack.views import SearchView
from django.views.static import serve
#from django.views import static

urlpatterns = [
    url(r'^$', views.blog_index),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace="blog")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
