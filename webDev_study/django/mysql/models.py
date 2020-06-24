from django.db import models


# Create your models here.
# 数据库在这里设置
# 字段名不能是PYTHON关键字 不能使用连续的下划线
# 自定义模型必须继承model
class TestMysql(models.Model):
    # db_column: 数据库表中的字段名称
    uid = models.AutoField(primary_key=True, db_column='uid')  # 设置主建自增长
    username = models.CharField(max_length=30, unique=True)  # charfield 指定长度
    password = models.CharField(max_length=128)  # 密码长一点
    rqtime = models.DateTimeField(auto_now_add=True)  # 第一次创建的时候定义时间

    class Meta:  # 元数据 模型本身的信息 跟表里的字段没有关联
        # 如果没指定 会有个默认表名: 应用名 模型名
        db_table = 'apptest'  # 模型对应的表明
        ordering = ['username']  # 排序 默认升序
