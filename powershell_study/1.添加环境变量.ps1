# 永久全局修改windows10系统环境变量
$oldValue = [environment]::GetEnvironmentVariable('game', 'user') # 获取数据
$newvalue = $oldValue + ';c:\windows' #拼接字符串
[environment]::SetEnvironmentvariable("game", $newvalue, "machine") #设置环境变量 user machine