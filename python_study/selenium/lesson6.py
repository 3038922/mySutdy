# radio checkbox 等选项的选择
# 导入Select类
from selenium.webdriver.support.ui import Select
from selenium import webdriver
# 打开chrome驱动
wd = webdriver.Chrome('./chromedriver.exe')
# 隐式等待 每隔半秒查一次 最大的等待时间10秒
wd.implicitly_wait(10)

# 按次序选择节点
wd.get("http://cdn1.python3.vip/files/selenium/test2.html")
#########################################
# radio
# 获取当前选中的元素
element = wd.find_element_by_css_selector(
    '#s_radio input[checked=checked]')
print('当前选中的是: ' + element.get_attribute('value'))

# 点选 小雷老师
wd.find_element_by_css_selector(
    '#s_radio input[value="小雷老师"]').click()
#####################################################
# chickbox
# 全选
eles = wd.find_elements_by_css_selector('#s_checkbox input')
for ele in eles:
    if (ele.get_attribute('checked') != 'true'):  # get_attribute('checked') 很奇怪 返回的是None 和 true
        ele.click()

##################################
# select
ele = wd.find_element_by_css_selector('#ss_single [value="小江老师"]')
ele.click()


######################################
# 多选
# 创建Select对象
select = Select(wd.find_element_by_id("ss_multi"))

# 清除所有 已经选中 的选项
select.deselect_all()

# 选择小雷老师 和 小凯老师
select.select_by_visible_text("小雷老师")
select.select_by_visible_text("小凯老师")
