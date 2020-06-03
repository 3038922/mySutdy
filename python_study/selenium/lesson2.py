# 根据属性 找特征
# 测试网址 http://f.python3.vip/webauto/sample1.html
import time
from selenium import webdriver
# 打开chrome驱动
wd = webdriver.Chrome('./chromedriver.exe')
# 隐式等待 每隔半秒查一次 最大的等待时间10秒
wd.implicitly_wait(10)
# # 打开网址
# wd.get("http://f.python3.vip/webauto/sample1.html")
# # 在百度输入框里输入信息
# # 注意这里返回多个对象 用数组
# eles = wd.find_elements_by_class_name("animal")
# # 遍历输入对象的文本属性
# for it in eles:
#     print(it.text)
# 按标签查找
# tagName = wd.find_elements_by_tag_name("span")
# for it in tagName:
#     print(it.text)

# 自己的测试
wd.get("http://192.168.31.193:3000/")
time.sleep(1)
eles = wd.find_elements_by_class_name("item")
for it in eles:
    if it.text == "登录":
        it.click()
        break
user = wd.find_element_by_id("user_name")
user.send_keys("3038922")
time.sleep(1)
passwd = wd.find_element_by_id("password")
passwd.send_keys("Protoss103!")
time.sleep(1)
login = wd.find_element_by_tag_name("button")
login.click()
time.sleep(2)
wd.quit()
