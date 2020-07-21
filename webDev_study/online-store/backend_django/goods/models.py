from datetime import datetime
from django.db import models

# Create your models here.
class GoodsCategory(models.Model):
    """
    商品类别 有子类 会用到外键
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )
    name = models.CharField(deafult="", max_length=30, verbose_name="类别名", help_text="类别名")  # 名字
    code = models.CharField(deafult="", max_length=30, verbose_name="类别code", help_text="类别code")  # 类编码
    desc = models.TextField(deafult="", max_length=200, verbose_name="类别描述", help_text="类别描述")  #
    category_type = models.CharField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")  #什么级别的类
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父目录级别", help_text="父目录", related_name="sub_cat")  # 父类别可以为空
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")  # 是否显示在tab
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """
    品牌名
    """
    name = models.CharField(deafult="", max_length=30, verbose_name="品牌名", help_text="品牌名")  # 名字
    desc = models.TextField(deafult="", max_length=200, verbose_name="品牌描述", help_text="品牌描述")  #
    image = models.CharField(max_length=200, upload_to="brand/images/")  # 品牌图片上传的地方
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodS(models.Model):
    """
    商品
    """
    category = models.ForeignKey(GoodsCategory)
    goods_sn = models.CharField(max_length=30)
    name = models.CharField(deafult="", max_length=30, verbose_name="商品名称")
    click_num = models.IntegerField()
    sold_num = models.IntegerField()
    fav_num = models.IntegerField()
    goods_num = models.IntegerField()  # 库存数量
    market_price=models.FloatField()
    shop_price = models.FloatField()
    goods_brief=models.TextField() # 富文本描述
    goods_desc=