import openpyxl
from openpyxl.styles import Font, colors
from openpyxl.chart import (
    Reference,
    Series,
    PieChart,
    BarChart,
    BubbleChart
)
# 读取表格
wb = openpyxl.load_workbook("新世纪疫情日报.xlsx")
# 显示所有表单
dict1 = {"总数": 0, "详情": [["班级", "姓名", "晨检异常情况描述"]]}
dict2 = {"总数": 0, "详情": [["班级", "姓名", "接触时间", "接触人员名字", "接触人员去过哪里"]]}
dict3 = {"总数": 0, "详情": [["班级", "姓名", "接触时间", "接触人员名字", "接触人员去过哪里"]]}
dict4 = {"总数": 0, "因发热未到或请假": 0, "因咳嗽腹泄乏力请假人数": 0, "因其他原因请假人数": 0, "详情": [
    ["班级", "姓名", "是否发热", "是否咳嗽乏力腹泻呕吐等", "是否有重点疫区接触史", "请假原因"]]}
班级 = ""
for cell in wb["晨检异常登记"]["C"]:
    if(cell.value != "") and (cell.value != "姓名"):
        dict1["总数"] += 1
        for it in wb["主表"]["Q"]:
            if (str(it.value).find(cell.value) >= 0):
                班级 = str(wb["主表"].cell(it.row, 6).value) + \
                    str(wb["主表"].cell(it.row, 7).value)
        dict1["详情"].append(
            [班级, cell.value, wb["晨检异常登记"].cell(cell.row, 4).value])
for cell in wb["学生接触外省人员登记"]["C"]:
    if(cell.value != "") and (cell.value != "姓名"):
        dict2["总数"] += 1
        for it in wb["主表"]["Q"]:
            if (str(it.value).find(cell.value) >= 0):
                班级 = str(wb["主表"].cell(it.row, 6).value) + \
                    str(wb["主表"].cell(it.row, 7).value)
        dict2["详情"].append([班级, cell.value, wb["学生接触外省人员登记"].cell(cell.row, 4).value,  wb["学生接触外省人员登记"].cell(
            cell.row, 5).value,  wb["学生接触外省人员登记"].cell(cell.row, 6).value])
for cell in wb["家长接触重点疫区、境外登记"]["C"]:
    if(cell.value != "") and (cell.value != "姓名"):
        dict3["总数"] += 1
        for it in wb["主表"]["Q"]:
            if (str(it.value).find(cell.value) >= 0):
                班级 = str(wb["主表"].cell(it.row, 6).value) + \
                    str(wb["主表"].cell(it.row, 7).value)
        dict3["详情"].append([班级, cell.value, wb["家长接触重点疫区、境外登记"].cell(cell.row, 4).value, wb["家长接触重点疫区、境外登记"].cell(
            cell.row, 5).value, wb["家长接触重点疫区、境外登记"].cell(cell.row, 6).value])
for cell in wb["请假学生登记"]["C"]:
    if(cell.value != "") and (cell.value != "姓名"):
        dict4["总数"] += 1
        if(wb["请假学生登记"].cell(cell.row, 4).value != "否") and (wb["请假学生登记"].cell(cell.row, 4).value != "无"):
            dict4["因发热未到或请假"] += 1
        if(wb["请假学生登记"].cell(cell.row, 5).value != "否") and (wb["请假学生登记"].cell(cell.row, 5).value != "无"):
            dict4["因咳嗽腹泄乏力请假人数"] += 1
        for it in wb["主表"]["Q"]:
            if (str(it.value).find(cell.value) >= 0):
                班级 = str(wb["主表"].cell(it.row, 6).value) + \
                    str(wb["主表"].cell(it.row, 7).value)
        dict4["详情"].append([班级, cell.value, wb["请假学生登记"].cell(cell.row, 4).value, wb["请假学生登记"].cell(
            cell.row, 5).value, wb["请假学生登记"].cell(cell.row, 6).value,  wb["请假学生登记"].cell(cell.row, 7).value])
    else:
        wb["请假学生登记"].delete_rows(cell.row)
dict4["因其他原因请假人数"] = dict4["总数"] - dict4["因发热未到或请假"] - dict4["因咳嗽腹泄乏力请假人数"]
# EXCEL 新表
wbNEW = openpyxl.Workbook()
wbNEW.active.title = "晨检异常"
wbNEW.create_sheet("学生接触外省人员")
wbNEW.create_sheet("家长接触重点疫区、境外")
wbNEW.create_sheet("请假学生")
wbNEW.create_sheet("综合统计")

for cell in dict1["详情"]:
    wbNEW["晨检异常"].append(cell)

for cell in dict2["详情"]:
    wbNEW["学生接触外省人员"].append(cell)

for cell in dict3["详情"]:
    wbNEW["家长接触重点疫区、境外"].append(cell)

wbNEW["综合统计"].append(
    ["请假学生登记人数总数", "因发热未到或请假", "因咳嗽腹泄乏力请假人数", "因其他原因请假人数", "晨检异常人数总数", "学生接触外省人员登记人数总数", "家长接触重点疫区、境外登记人数总数"])
wbNEW["综合统计"].append([dict4["总数"], dict4["因发热未到或请假"],
                      dict4["因咳嗽腹泄乏力请假人数"], dict4["因其他原因请假人数"], dict1["总数"], dict2["总数"], dict3["总数"]])
for cell in dict4["详情"]:
    wbNEW["请假学生"].append(cell)

wbNEW.save("5.chart.xlsx")
