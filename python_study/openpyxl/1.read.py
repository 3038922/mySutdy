# coding=utf8
import os
import openpyxl
# 转换列为字母或者数字
from openpyxl.utils import get_column_letter, column_index_from_string

# wb = openpyxl.Workbook()  # 新建一个
wb = openpyxl.load_workbook("./1read.xlsx")  # 读取表格
ws = wb['Sheet']
print("该表总共:", ws.max_row, "行 * ", ws.max_column, "列.")
print("转换数字为字母:", get_column_letter(2), get_column_letter(47))
print("转换字母为数字:", column_index_from_string(
    "a"), column_index_from_string("BB"))
# 遍历输入
# sheet = wb["Sheet"]
# for row in range(1, 10):
#     for col in range(1, 10):
#         sheet.cell(row, col).value = row*col

# 单体输出测试
#str1 = 'A1'
# print(ws)
# print(ws[str1])
# print("[", ws[str1].row, ",", ws[str1].column, "]=", ws[str1].value)
# print(ws[3][2].value)
#print(ws.cell(1, 1).value)
# print("[", ws[str1].coordinate, "]=", ws[str1].value)


# 遍历输出
# for row in range(1, 10, 1):
#     for col in range(1, 10, 1):
#         print(ws.cell(row, col).value, end=" ")  # 不换行
#     print("")
# 输出整行
# col6 = ws[6]
# for it in col6:
#     print(it.value)

# 输出整列
# colA = ws["B"]
# for it in colA:
#     print(it.value)

# 切片输出
# rowRange = ws[2:6]
# colRange = ws['B:C']
# for col in colRange:
#     for cell in col:
#         print(cell.value, end=" ")
#     print("")
# for row in ws.iter_rows(min_row=1, max_row=2, min_col=1, max_col=2):
#     for cell in row:
#         print(cell.value, end=" ")
#     print("")
# for row in ws["A1:C3"]:
#     for cell in row:
#         print("[", cell.coordinate, "]=", cell.value, end=" ")
#     print("")

# 保存
# wb.save('demo.xlsx')
