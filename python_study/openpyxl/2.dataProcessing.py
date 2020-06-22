# coding=utf8
import os
import openpyxl
import re
from openpyxl.styles import Font
from openpyxl.styles import colors
# 转换列为字母或者数字
from openpyxl.utils import get_column_letter, column_index_from_string

wb = openpyxl.load_workbook("./新世纪学校班级晨检、日报表（每天上午9-00前填报，包括双休日）.xlsx")
请假学生明细 = wb.active
请假学生明细.title = '请假学生明细'
print("该表总共:", 请假学生明细.max_row, "行 * ", 请假学生明细.max_column, "列.")
print("当前表单页为:", 请假学生明细.title)

# name = [["提交人", "填写周期", "班级", "请假学生姓名", "请详细说明学生请假原因"]]
total = []*6
cutName = re.compile(r'[  ,   、， ]')  # 分割学生名字正则表达式
# 按第一行内容搜索
for col in 请假学生明细["O"]:
    if col.value != "无" and col.value != "0":
        temp = re.split(cutName, 请假学生明细[col.row]
                        [column_index_from_string("O")-1].value)
        for it in temp:
            # 无 0 替换成否
            请假学生明细[col.row][column_index_from_string(
                "Q")-1].value = 请假学生明细[col.row][column_index_from_string("Q")-1].value.replace("0", "否").replace("无", "否").replace("均否", "否").replace(it, "")
            total.append([请假学生明细[col.row][0].value, 请假学生明细[col.row][4].value, 请假学生明细[col.row][8].value,
                          it, 请假学生明细[col.row][column_index_from_string("P")-1].value, 请假学生明细[col.row][column_index_from_string("Q")-1].value])

# 新建一个
newWB = openpyxl.Workbook()
new请假学生明细 = newWB.active
# 格式调整
new请假学生明细.column_dimensions["B"].width = 20  # 第B列宽度
new请假学生明细.column_dimensions["C"].width = 20  # 第B列宽度
new请假学生明细.column_dimensions["D"].width = 20  # 第B列宽度
new请假学生明细.column_dimensions["E"].width = 70  # 第B列宽度
new请假学生明细.column_dimensions["F"].width = 40  # 第B列宽度
# 按行添加
for row in total:
    new请假学生明细.append(row)
# 保存
newWB.save('./demo.xlsx')
