from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserInfo(models.Model):
    """
    用户信息
    """
    headImg = models.ImageField()  # 头像字段
    nickName = models.CharField(max_length=12)  # 昵称 最大12个字
    belong = models.OneToOneField(User, on_delete=models.CASCADE)  # 关联USER表单

    def __init__(self):
        return self.id


class Category(models.Model):
    """
    文章分类 复杂 递归分类
    """
    names = models.CharField(max_length=12)  # 分类名称

    #belong = models.ForeignKey(self, on_delete=models.CASCADE)  # 一对多的关联 递归

    def __init__(self):
        return self.id


class Article(models.Model):
    """
    文章
    """
    title = models.CharField(max_length=12)  # 标题
    cover = models.CharField(max_length=36)  # 图片的字段
    text = models.TextField()  # 文本内容
    belong = models.ForeignKey(UserInfo, on_delete=models.CASCADE)  # 一对多的关联

    def __init__(self):
        return self.id


class Favourite(models.Model):
    """
    收藏
    """
    belong_user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)  #一对多 关联用户
    belong_art = models.ForeignKey(Article, on_delete=models.CASCADE)  #一对多  关联文章

    def __init__(self):
        return self.idLike


class Like(models.Model):
    """
    点赞 (其实收藏跟收藏是一样的)
    """
    belong_user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)  #一对多 关联用户
    belong_art = models.ForeignKey(Article, on_delete=models.CASCADE)  #一对多  关联文章

    # num = models.IntegerField()  # 点赞次数 点一下自增1

    def __init__(self):
        return self.ids


class PayOrder(models.Model):
    """
    打赏
    """
    order = models.CharField(max_length=12)  #  订单号
    price = models.CharField(max_length=12)  #  金额
    status = models.BooleanField()  # 状态 BOOL值

    def __init__(self):
        return self.id