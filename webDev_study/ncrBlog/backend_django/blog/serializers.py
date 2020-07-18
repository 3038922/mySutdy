from rest_framework import serializers
from blog.models import *


class CommentmetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentmeta
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = '__all__'


class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = '__all__'


class PostmetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postmeta
        fields = '__all__'


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'


class TermRelationshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermRelationships
        fields = '__all__'


class TermTaxonomySerializer(serializers.ModelSerializer):
    class Meta:
        model = TermTaxonomy
        fields = '__all__'


class TermmetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Termmeta
        fields = '__all__'


class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms
        fields = '__all__'


class UsermetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usermeta
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'