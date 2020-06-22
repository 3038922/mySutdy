import openpyxl
# 创建新工作表
wb = openpyxl.Workbook()
# 工作簿处理
test1 = wb.active
test1.title = "test1"
wb.create_sheet(index=0, title='test0')
wb.create_sheet(index=2, title='test2')
print(wb.get_sheet_names())

# 单元写输入
# 按列添加
testData = [[0]*5]*5
for row in testData:
    test1.append(row)


# 保存
wb.save('3.writhe.xlsx')
