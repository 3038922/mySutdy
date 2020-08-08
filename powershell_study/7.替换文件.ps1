# 获取python包安装路径
$targetPath = "C:\Users\$env:UserName\AppData\Local\Programs\Python\Python38\Lib\site-packages\pros\common\ui\"
$tmpFileName = '.\__init__.py'
Write-Host  $targetPath -ForegroundColor Green
Move-Item -Path $tmpFileName -Destination $targetPath -Force