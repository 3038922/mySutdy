# 操作嵌入的文档
# 按次序选择子节点
from selenium import webdriver
# 打开chrome驱动
wd = webdriver.Chrome('./chromedriver.exe')
# 隐式等待 每隔半秒查一次 最大的等待时间10秒
wd.implicitly_wait(10)

# 按次序选择节点
wd.get("http://f.python3.vip/webauto/sample2.html")
# 切换到内层进行操作 参数写ID 等什么都可以
# wd.switch_to.frame("frame1")
# 如果没有ID什么的 注意这里是element 不是elements
wd.switch_to.frame(wd.find_element_by_css_selector('[src="sample1.html"]'))

eles = wd.find_elements_by_css_selector(".plant")
for ele in eles:
    print(ele.get_attribute("outerHTML"))
# 切换到外层
wd.switch_to_default_content()

# 切换到新的窗口
js = 'window.open("http://f.python3.vip/webauto/sample3.html")'
wd.execute_script(js)
handlers = wd.window_handles  # 获取当前页面的句柄
wd.switch_to_window(handlers[1])  # 切换第几个 0开始
# 点击打开新窗口的链接
link = wd.find_element_by_tag_name('a')
link.click()
print(wd.title)
# 保存上个网页的句柄
mainHandle = wd.current_window_handle
# 切换到新标签的句柄
for handle in wd.window_handles:
    wd.switch_to.window(handle)
    if "Bing" in wd.title:
        print("找到了:", wd.title, "标签页,正在切换")
        break
wd.switch_to.window(mainHandle)
wd.close()  # 关闭当前标签页
wd.quit()  # 退出
