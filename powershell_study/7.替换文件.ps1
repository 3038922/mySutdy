# 获取python包安装路径
$targetPath = "C:\Users\$env:UserName\AppData\Local\Programs\Python\Python38\Lib\site-packages\pros\common\ui\"
$tmpFileName = '.\__init__.py'
Write-Host  $targetPath -ForegroundColor Green
Copy-Item -Path $tmpFileName -Destination $targetPath -Force

$targetPath = "C:\Users\$env:UserName\AppData\Roaming\PROS\templates"
$tmpFileName = '.\kernel@3.2.1'
Write-Host  $targetPath -ForegroundColor Green
Copy-Item -Path $tmpFileName -Destination $targetPath -Recurse -Force

$targetPath = "C:\Users\$env:UserName\AppData\Roaming\PROS\templates"
$tmpFileName = '.\okapilib@4.0.4'
Write-Host  $targetPath -ForegroundColor Green
Copy-Item -Path $tmpFileName -Destination $targetPath -Recurse -Force

# Expand-Archive -Path .\extern_script.zip -DestinationPath  .\ -Force