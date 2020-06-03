# 通过CSS表达式来选择
from selenium import webdriver
# 打开chrome驱动
wd = webdriver.Chrome('./chromedriver.exe')
# 隐式等待 每隔半秒查一次 最大的等待时间10秒
wd.implicitly_wait(10)
# # 打开网址
print("----------------------find by style----------------")
wd.get("http://f.python3.vip/webauto/sample1.html")
eles = wd.find_elements_by_css_selector(".animal")
for ele in eles:
    print(ele.get_attribute('outerHTML'))

print("----------------------find by tagname----------------")
# 搜标签名 比如<span>
eles = wd.find_elements_by_css_selector("span")
for ele in eles:
    print(ele.get_attribute('outerHTML'))

print("----------------------find by id----------------")  # 表示 ID=什么的
# 搜标id
eles = wd.find_elements_by_css_selector("#searchtext")
for ele in eles:
    print(ele.get_attribute('outerHTML'))

print("----------------------find by tagname > " " 的作用----------------")
# 搜标id
eles = wd.find_elements_by_css_selector("#layer1 span")  # 空格可以跨级查 > 是逐级查
for ele in eles:
    print(ele.text)

print("----------------------find by 位置---------------")  # . 表示CLASS=什么
# 搜标id
eles = wd.find_elements_by_css_selector(".plant span")  # 空格可以跨级查 > 是逐级查
for ele in eles:
    print(ele.text)

print("----------------------find by 万能属性寻找法---------------")  # . 表示CLASS=什么
# 搜标id
# 空格可以跨级查 > 是逐级查
eles = wd.find_elements_by_css_selector('[href="http://www.miitbeian.gov.cn"]')
for ele in eles:
    print("text:", ele.text, "\n",
          "get_attribute:", ele.get_attribute('outerHTML'))

print("----------------------find by 万能属性寻找法 唯一属性---------------")  # . 表示CLASS=什么
# 搜标id
# 空格可以跨级查 > 是逐级查
eles = wd.find_elements_by_css_selector('[href]')
for ele in eles:
    print("text:", ele.text, "\n",
          "get_attribute:", ele.get_attribute('outerHTML'))


print("----------------------find by 万能属性寻找法 组合使用--------------")  # . 表示CLASS=什么
# 搜标id
# 空格可以跨级查 > 是逐级查
eles = wd.find_elements_by_css_selector('div[class="plant"]')  # 别加空格
for ele in eles:
    print("text:", ele.text, "\n",
          "get_attribute:", ele.get_attribute('outerHTML'))
wd.quit()
