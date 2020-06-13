# 按次序选择子节点
from selenium import webdriver
# 打开chrome驱动
wd = webdriver.Chrome('./chromedriver.exe')
# 隐式等待 每隔半秒查一次 最大的等待时间10秒
wd.implicitly_wait(10)

# 按次序选择节点
wd.get("http://f.python3.vip/webauto/sample1b.html")

# span:nth-child(2) 父元素里span类型的第二个子节点
# #t1:nth-child(2) id t1 里 第二个子节点
# p:nth-last-child(1) p类型的 里 最后一个子节点
# nth-of-type 我们可以指定选择的元素 是父元素的第几个 某个类型 的子节点
# 如: span:nth-of-type(1) 第一个span类型的子元素
# 奇数 偶数模式选择
# nth-child(odd) 奇数
# p:nth-of-type(even) p类型的偶数

# 兄弟节点 +
# 例:  h3+span 紧跟后面的span
# 例:  h3~span h3后面所有的span
# 还需要搜 css语法选择器
