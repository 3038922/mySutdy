import openpyxl
from openpyxl.styles import Font
from openpyxl.styles import colors

wb = openpyxl.Workbook()
# font
ws = wb.active
ws.title = "Font"
# 建立模拟数据
total = []*9
for col in range(1, 10):
    for row in range(1, 10):
        ws.cell(col, row).value = col * row

# 设置你需要的字体
italic24Font = Font(size=24, italic=True)
ws['A1'].font = italic24Font
ws['A1'] = '24pt Italic'

boldRedFont = Font(name="Times New Roman", bold=True, color=colors.RED)
# 可以直接套EXCEL 内置公式
ws['B9'] = "=SUM(B1:B8)"
ws['B9'].font = boldRedFont

# 改变行高度和宽度
ws.row_dimensions[2].height = 70  # 第二行高度
ws['A2'] = "Tall row"
ws.column_dimensions["B"].width = 20  # 第B列宽度
ws.row_dimensions[1].width = 20  # 第一行宽度 无效
ws['A3'] = "Wide col"
# 合并单元格
ws.merge_cells('A1:D1')
ws['A1'] = 'TEST'

# 拆分单元格
newWs = wb.copy_worksheet(wb["Font"])  # 拷贝表达
newWs.title = "unmerged"
newWs.unmerge_cells('A1:D1')  # 这里似乎必须按原来几个合并 就拆分成几个
newWs['A1'] = 'unmerged test'
# 保存
wb.save("4.style.xlsx")
for it in range(1, 101, 1):
    print("hello wrold")
