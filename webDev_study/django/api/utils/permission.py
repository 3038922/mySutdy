from rest_framework.permissions import BasePermission
"""
访问权限控制
"""


class SVIPMyPermission(BasePermission):
    """
    权限模块
    注意继承 BasePermission
    """
    message = '必须是SVIP才能访问'

    def has_permission(self, request, view):
        if request.user.user_type != 3:
            return False
        return True


class MyPermission1(BasePermission):
    """
    权限模块
    """
    def has_permission(self, request, view):
        if request.user.user_type == 3:
            return False
        return True
