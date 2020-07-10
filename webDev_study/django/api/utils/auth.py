from rest_framework import exceptions
from api import models
from rest_framework.authentication import BaseAuthentication  # rest_framework 里的写好的认证类


class FirstAuthtication(BaseAuthentication):
    """
    最好继承rest_framework里的认证类
    """
    def authenticate(self, request):
        pass

    def authenticate_header(self, request):
        pass


class Authtication(BaseAuthentication):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户验证失败')
        # 在rest_framework内部会将整个两个字段复制给request 以供后续操作使用
        return (token_obj.user, token_obj)

    def authenticate_header(self, request):
        return 'basic realm="api"'
