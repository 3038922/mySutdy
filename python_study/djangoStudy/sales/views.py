# from django.shortcuts import render
from django.http import HttpResponse
from common.models import Customer
# Create your views here.


def listorders(request):
    return HttpResponse("hello wrold")


html_template = '''
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <style>
        table {
            border-collapse: collapse;
        }

        th,
        td {
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
    </style>
</head>

<body>
    <table>
        <tr>
            <th>id</th>
            <th>姓名</th>
            <th>电话号码</th>
            <th>地址</th>
            <th>QQ</th>
        </tr>

        %s



    </table>
</body>

</html>
'''


def listcustomers(request):
    # 返回一个QuerySet对象
    # 每条记录都是一个dict对象
    # key 是字段名 value是字段值
    qs = Customer.objects.values()
    # 检查url中是否有参数 phonenumber
    ph = request.GET.get('phonenumber', None)
    # 如果有 添加过滤条件
    if ph:
        qs = qs.filter(phonenumber=ph)
    # 生成html模板中要插入的html片段内容
    tableCOntent = ''
    for customer in qs:
        tableCOntent += '<tr>'
        for name, value in customer.items():
            tableCOntent += f'<td>{value}</td>'

        tableCOntent += '</tr>'  # <br> 表示换行
    return HttpResponse(html_template % tableCOntent)
