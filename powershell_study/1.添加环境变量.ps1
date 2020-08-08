# 永久全局修改windows10系统环境变量
$oldValue = [environment]::GetEnvironmentVariable('Path', 'machine') # 获取数据
$newvalue = $oldValue + 'c:\windows;' + 'c:\test;' #拼接字符串
Write-Host "$newvalue" -ForegroundColor Green

# [environment]::SetEnvironmentvariable("Path", $newvalue, "machine") #设置环境变量 user machine