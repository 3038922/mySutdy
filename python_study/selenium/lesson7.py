# 鼠标右键 双击 移动到某个元素 拖拽等
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
# 如果我们把鼠标放在上边，就会弹出 下面的 糯米、音乐、图片 等图标。

# 使用 ActionChains 来 模拟鼠标移动 操作的代码如下：
driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(5)

driver.get('https://www.baidu.com/')


ac = ActionChains(driver)

# 鼠标移动到 元素上
ac.move_to_element(
    driver.find_element_by_css_selector('[name="tj_briicon"]')
).perform()
# 直接执行javascript
# 直接执行 javascript，里面可以直接用return返回我们需要的数据
nextPageButtonDisabled = driver.execute_script(
    '''
    ele = document.querySelector('.soupager > button:last-of-type');
    return ele.getAttribute('disabled')
    ''')

# 返回的数据转化为Python中的数据对象进行后续处理
# if nextPageButtonDisabled == 'disabled':  # 是最后一页
#     return True
# else:  # 不是最后一页
#     return False
# 有些网站上面的元素， 我们鼠标放在上面，会动态弹出一些内容。移开就会消失
# 在 开发者工具栏 console 里面执行如下js代码

# setTimeout(function(){debugger}, 5000)
#####################################################
# 弹出对话框
driver.get('http://cdn1.python3.vip/files/selenium/test4.html')
# --- alert ---
driver.find_element_by_id('b1').click()

# 打印 弹出框 提示信息
print(driver.switch_to.alert.text)

# 点击 OK 按钮
driver.switch_to.alert.accept()
#################################################
# --- confirm ---
driver.find_element_by_id('b2').click()

# 打印 弹出框 提示信息
print(driver.switch_to.alert.text)

# 点击 OK 按钮
driver.switch_to.alert.accept()

driver.find_element_by_id('b2').click()

# 点击 取消 按钮
driver.switch_to.alert.dismiss()

###############################################
# --- prompt ---
driver.find_element_by_id('b3').click()

# 获取 alert 对象
alert = driver.switch_to.alert

# 打印 弹出框 提示信息
print(alert.text)

# 输入信息，并且点击 OK 按钮 提交
alert.send_keys('web自动化 - selenium')
alert.accept()

# 点击 Cancel 按钮 取消
driver.find_element_by_id('b3').click()
alert = driver.switch_to.alert
alert.dismiss()
# 更多
# http://www.python3.vip/tut/auto/selenium/skills_2/
