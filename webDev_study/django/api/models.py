from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'oldboy_book'
        verbose_name = '书籍'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<<%s>>' % self.title


# 用户级别
class UserInfo(models.Model):
    user_type_choices = (
        (1, '普通用户'),
        (2, 'VIP'),
        (3, 'SVIP'),
    )
    user_type = models.IntegerField(choices=user_type_choices)
    username = models.CharField(max_length=32, unique=True)  # unique 用户名是唯一的
    password = models.CharField(max_length=64)


# 创建token
class UserToken(models.Model):
    user = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    token = models.CharField(max_length=64)