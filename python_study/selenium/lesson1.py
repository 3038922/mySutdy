from selenium import webdriver
# 打开chrome驱动
wd = webdriver.Chrome('./chromedriver.exe')
# 打开网址
wd.get("https://www.baidu.com")
# 在百度输入框里输入信息
# 首先要选择元素
# BY ID
element = wd.find_element_by_id("kw")
# 输入内容
element.send_keys("陈昱安")
# 找到点击按钮
element = wd.find_element_by_id("su")
# 点击
element.click()
