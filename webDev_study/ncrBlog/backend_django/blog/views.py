from rest_framework import serializers, viewsets
from blog.models import Articles

# Create your views here.


class ArticlesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articles  # 指定的模型类
        fields = ('id', 'title', 'body', 'timestamp', 'authorname', 'views', 'tags', 'category')  # 需要序列化的属性


class GetArticleInfo(viewsets.ModelViewSet):
    queryset = Articles.objects.all().order_by('-id')
    serializer_class = ArticlesSerializers
