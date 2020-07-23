from datetime import datetime
from django.db import models
#from DjangoUeditor.models import UEditorField
from tinymce.models import HTMLField


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
    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")  # 名字
    code = models.CharField(default="", max_length=30, verbose_name="类别code",
                            help_text="类别code")  # 类编码
    desc = models.TextField(default="", max_length=200, verbose_name="类别描述", help_text="类别描述")  #
    category_type = models.CharField(max_length=200,
                                     choices=CATEGORY_TYPE,
                                     verbose_name="类目级别",
                                     help_text="类目级别")  #什么级别的类
    parent_category = models.ForeignKey("self",
                                        null=True,
                                        blank=True,
                                        verbose_name="父目录级别",
                                        help_text="父目录",
                                        related_name="sub_cat",
                                        on_delete=models.CASCADE)  # 父类别可以为空
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
    name = models.CharField(default="", max_length=30, verbose_name="品牌名", help_text="品牌名")  # 名字
    desc = models.TextField(default="", max_length=200, verbose_name="品牌描述", help_text="品牌描述")  #
    image = models.ImageField(max_length=200, upload_to="brand/images/")  # 品牌图片上传的地方
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    商品
    """
    category = models.ForeignKey(GoodsCategory,
                                 null=True,
                                 blank=True,
                                 verbose_name="商品类目",
                                 help_text="商品类目",
                                 on_delete=models.CASCADE)
    goods_sn = models.CharField(max_length=50, default="", verbose_name="商品唯一编号")
    name = models.CharField(default="", max_length=30, verbose_name="商品名称")
    click_num = models.IntegerField(default=0, verbose_name="商品点击数")
    sold_num = models.IntegerField(default=0, verbose_name="商品销售量")
    fav_num = models.IntegerField(default=0, verbose_name="商品收藏数")
    goods_num = models.IntegerField(default=0, verbose_name="商品库存数")  # 库存数量
    market_price = models.FloatField(default=0, verbose_name="市场价格")
    shop_price = models.FloatField(default=0, verbose_name="本店价格")
    goods_brief = models.TextField(max_length=500, verbose_name="商品简短描述")  # 富文本描述
    # goods_desc = UEditorField(verbose_name=u"内容",
    #                           imagePath="goods/images/",
    #                           width=1000,
    #                           height=300,
    #                           filePath="goods/files/",
    #                           default="")
    goods_desc = HTMLField()
    ship_free = models.BooleanField(default=True, verbose_name="是否承担运费")  # 是否免运费
    goods_front_image = models.ImageField(upload_to="", null=True, blank=True, verbose_name="封面图")
    is_new = models.BooleanField(default=False, verbose_name="是否新品")  # 是否新品
    is_hot = models.BooleanField(default=False, verbose_name="是否热卖")  # 是否热卖
    add_time = models.DateTimeField(default=datetime.now, verbose_name="商品添加时间")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    """
    一对多关系必须建表了
    商品轮播图
    """
    goods = models.ForeignKey(Goods,
                              verbose_name="商品",
                              related_name="images",
                              on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", null=True, blank=True, verbose_name="图片")
    image_url = models.CharField(max_length=300, null=True, blank=True, verbose_name="图片url")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """
    轮播的商品
    """
    goods = models.ForeignKey(Goods, verbose_name="商品", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="banner", verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name
