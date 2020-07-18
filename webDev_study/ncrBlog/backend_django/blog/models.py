import django.utils.timezone as timezone
from django.db import models


class Commentmeta(models.Model):
    """
    评论数据元
    """
    meta_id = models.AutoField(primary_key=True, verbose_name='自增ID')
    comment_id = models.BigIntegerField(verbose_name='评论ID')
    meta_key = models.CharField(max_length=255, blank=True, null=True, verbose_name='key')
    meta_value = models.TextField(blank=True, null=True, verbose_name='value')

    class Meta:
        #       managed = False
        db_table = 'commentmeta'


class Comments(models.Model):
    """
    评论
    """
    comment_id = models.AutoField(primary_key=True, verbose_name='自增ID')  # Field name made lowercase.
    comment_post_id = models.BigIntegerField(verbose_name='文章ID')  # Field name made lowercase.
    comment_author = models.TextField(verbose_name='作者')
    comment_author_email = models.CharField(max_length=100, verbose_name='作者邮箱')
    comment_author_url = models.CharField(max_length=200, verbose_name='作者链接')
    comment_author_ip = models.CharField(max_length=100, verbose_name='作者IP')  # Field name made lowercase.
    comment_date = models.DateTimeField(verbose_name='评论时间', default=timezone.now)
    comment_date_gmt = models.DateTimeField(verbose_name='评论时间GMT', default=timezone.now)
    comment_content = models.TextField(verbose_name='评论内容')
    comment_karma = models.IntegerField(verbose_name='未使用', blank=True)
    comment_approved = models.CharField(max_length=20, verbose_name='评论状态(是否被批准)')
    comment_agent = models.CharField(max_length=255, verbose_name='用户USERAGENT')
    comment_type = models.CharField(max_length=20, verbose_name='评论状态(pingback引用/普通)')
    comment_parent = models.BigIntegerField(verbose_name='父ID(评论)', blank=True)
    user_id = models.BigIntegerField(verbose_name='用户ID')

    class Meta:
        #       managed = False
        db_table = 'comments'


class Links(models.Model):
    """
    链接(友链或者导航链接)
    """
    link_id = models.AutoField(primary_key=True, verbose_name='自增ID')
    link_url = models.CharField(max_length=255, verbose_name='链接URL')
    link_name = models.CharField(max_length=255, verbose_name='连接标题')
    link_image = models.CharField(max_length=255, verbose_name='链接图片')
    link_target = models.CharField(max_length=25, verbose_name='图片打开方式')
    link_description = models.CharField(max_length=255, verbose_name='链接描述')
    link_visible = models.CharField(max_length=20, verbose_name='是否可见')
    link_owner = models.BigIntegerField(verbose_name='添加者用户ID')
    link_rating = models.IntegerField(verbose_name='评分等级')
    link_updated = models.DateTimeField(verbose_name='更新时间', default=timezone.now)
    link_rel = models.CharField(max_length=255, verbose_name='XFN关系')
    link_notes = models.TextField(verbose_name='XFN注释')
    link_rss = models.CharField(max_length=255, verbose_name='链接rss地址')

    class Meta:
        #       managed = False
        db_table = 'links'


class Options(models.Model):
    """
    博客设置数据元
    """
    option_id = models.AutoField(primary_key=True, verbose_name='自增ID')
    option_name = models.CharField(unique=True, max_length=191, verbose_name='key')
    option_value = models.TextField(verbose_name='value')
    autoload = models.CharField(max_length=20, verbose_name='是否在博客加载时自动载入')

    class Meta:
        #       managed = False
        db_table = 'options'


class Postmeta(models.Model):
    """
    文章数据元
    """
    meta_id = models.AutoField(primary_key=True, verbose_name='自增ID')
    post_id = models.BigIntegerField(verbose_name='文章ID')
    meta_key = models.CharField(max_length=255, blank=True, null=True, verbose_name='key')
    meta_value = models.TextField(blank=True, null=True, verbose_name='value')

    class Meta:
        #       managed = False
        db_table = 'postmeta'


class Posts(models.Model):
    """
    文章
    """
    post_id = models.AutoField(primary_key=True, verbose_name='自增ID')  # Field name made lowercase.
    post_author = models.BigIntegerField(verbose_name='作者ID')
    post_date = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    post_date_gmt = models.DateTimeField(verbose_name='发布时间GMT', auto_now_add=True)
    post_content = models.TextField(verbose_name='正文')
    post_title = models.TextField(verbose_name='标题')
    post_excerpt = models.TextField(verbose_name='摘要')
    post_status = models.CharField(max_length=20, verbose_name='文章状态')
    comment_status = models.CharField(max_length=20, verbose_name='评论状态')
    ping_status = models.CharField(max_length=20, verbose_name='ping状态')
    post_password = models.CharField(max_length=255, verbose_name='文章密码')
    post_name = models.CharField(max_length=200, verbose_name='文章缩略名')
    to_ping = models.TextField(verbose_name='未使用')
    pinged = models.TextField(verbose_name='已经ping过得链接')
    post_modified = models.DateTimeField(verbose_name='修改时间', default=timezone.now)
    post_modified_gmt = models.DateTimeField(verbose_name='修改时间GMT', default=timezone.now)
    post_content_filtered = models.TextField(verbose_name='未使用')
    post_parent = models.BigIntegerField(verbose_name='父文章')
    guid = models.CharField(max_length=255, verbose_name='GUID')
    menu_order = models.IntegerField(verbose_name='排序ID')
    post_type = models.CharField(max_length=20, verbose_name='文章类型')
    post_mime_type = models.CharField(max_length=100, verbose_name='MIME类型')
    comment_count = models.BigIntegerField(verbose_name='评论总数')

    class Meta:
        #       managed = False
        db_table = 'posts'


class TermRelationships(models.Model):
    """
    分类关系(表示一个对象属于哪个分类)
    http://www.wptoutiao.com/tutorial/629.html
    字段object_id是对象ID,关联表wp_posts表,term_taxonomy_id字段是分类ID,关联wp_term_taxonomy表ID,也就是描述对象属于哪个分类，比如：
    文章属于哪个分类
    菜单项属于哪个菜单
    """
    object_id = models.AutoField(primary_key=True, verbose_name='对象ID')
    term_taxonomy_id = models.BigIntegerField(verbose_name='分类ID')
    term_order = models.IntegerField(verbose_name='分类排序')

    class Meta:
        #       managed = False
        db_table = 'term_relationships'
        unique_together = (('object_id', 'term_taxonomy_id'), )


class TermTaxonomy(models.Model):
    """
    分类系统(用来存储分类系统的一些属性)
    http://www.wptoutiao.com/tutorial/584.html
    """
    term_taxonomy_id = models.AutoField(primary_key=True, verbose_name='自增ID')
    term_id = models.BigIntegerField(verbose_name='对应wp_terms表中的ID')
    taxonomy = models.CharField(max_length=32, verbose_name='表示分类系统')
    description = models.TextField(verbose_name='分类头像描述')
    parent = models.BigIntegerField(verbose_name='父分类ID')
    count = models.BigIntegerField(verbose_name='分类下内容数量')

    class Meta:
        #       managed = False
        db_table = 'term_taxonomy'
        unique_together = (('term_id', 'taxonomy'), )


class Termmeta(models.Model):
    """
    分类和标签
    http://www.wptoutiao.com/tutorial/569.html
    """
    meta_id = models.AutoField(primary_key=True, verbose_name='自增ID')
    term_id = models.BigIntegerField(verbose_name='分类ID')
    meta_key = models.CharField(max_length=255, blank=True, null=True, verbose_name='key')
    meta_value = models.TextField(blank=True, null=True, verbose_name='value')

    class Meta:
        #       managed = False
        db_table = 'termmeta'


class Terms(models.Model):
    """
    分类信息(用来存储网站的文章分类目录，标签等分类信息)
    http://www.wptoutiao.com/tutorial/555.html
    """
    term_id = models.AutoField(primary_key=True, verbose_name='自增ID')
    name = models.CharField(max_length=200, verbose_name='分类名称')
    slug = models.CharField(max_length=200, verbose_name='分类别名')
    term_group = models.BigIntegerField(verbose_name='分类分组')

    class Meta:
        #       managed = False
        db_table = 'terms'


class Usermeta(models.Model):
    """
    用户数据元
    """
    umeta_id = models.AutoField(primary_key=True, verbose_name='自增ID')
    user_id = models.BigIntegerField(verbose_name='用户ID')
    meta_key = models.CharField(max_length=255, blank=True, null=True, verbose_name='key')
    meta_value = models.TextField(blank=True, null=True, verbose_name='value')

    class Meta:
        #       managed = False
        db_table = 'usermeta'


class Users(models.Model):
    """
    用户
    """
    user_id = models.AutoField(primary_key=True, verbose_name='自增ID')  # Field name made lowercase.
    user_login = models.CharField(max_length=60, verbose_name='用户名')
    user_pass = models.CharField(max_length=255, verbose_name='密码')
    user_nicename = models.CharField(max_length=50, verbose_name='昵称')
    user_email = models.CharField(max_length=100, verbose_name='电子邮件')
    user_url = models.CharField(max_length=100, verbose_name='网址')
    user_registered = models.DateTimeField(verbose_name='注册时间', auto_now_add=True)
    user_activation_key = models.CharField(max_length=255, verbose_name='激活码', blank=False, null=True)
    user_status = models.IntegerField(verbose_name='用户状态')
    display_name = models.CharField(max_length=250, verbose_name='显示名称')

    class Meta:
        #       managed = False
        db_table = 'users'
