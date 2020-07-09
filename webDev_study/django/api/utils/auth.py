from rest_framework import exceptions
from api import models


class FirstAuthtication(object):
    def authenticate(self, request):
        pass

    def authenticate_header(self, request):
        pass


class Authtication(object):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        print('obj_test:', models.UserToken.objects.filter(token=token).first)
        token_obj = models.UserToken.objects.filter(token=token).first
        if not token_obj:
            raise execeptions.AuthenticationFailed('用户验证失败')
        # 在rest_framework内部会将整个两个字段复制给request 以供后续操作使用
        return (token_obj.user, token_obj)

    def authenticate_header(self, request):
        pass