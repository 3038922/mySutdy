
# Powershell 中的比较运算符
# -eq ：等于
# -ne ：不等于
# -gt ：大于
# -ge ：大于等于
# -lt ：小于
# -le ：小于等于
# -contains ：包含
# -notcontains :不包含

# 布尔运算
# 
# -and ：和
# -or ：或
# -xor ：异或
# -not ：逆

$flag1 = Test-Path C:\Scripts\Archive
if ($flag1 -eq 'True') {
    Write-Host $flag1 -ForegroundColor Green
}
else {
    Write-Host $flag1 -ForegroundColor Red
}

$flag2 = Test-Path C:\temp\1.txt

if ($flag2 -eq 'True') {
    Write-Host $flag2 -ForegroundColor Green
}
else {
    Write-Host $flag2 -ForegroundColor Red
}
