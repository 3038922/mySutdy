# 永久全局修改windows10系统环境变量
$path = [environment]::GetEnvironmentVariable('Path', 'machine') # 获取数据
$addPath = @('C:\Program Files\Git\cmd', 'c:\test', 'c:\windows')

foreach ($it in $addPath) { 
    if ($path.split(";") -Contains $it) {
        Write-Host "路径: $it 已存在" -ForegroundColor yellow 
    }
    else {
        $path += ($it + ";")
        Write-Host "路径: $it 已添加" -ForegroundColor green 
    }
}
Write-Host "$path" -ForegroundColor Green

#[environment]::SetEnvironmentvariable("Path", $newvalue, "machine") #设置环境变量 user machine