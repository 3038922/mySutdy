# 1. PS命令解压
# 前提:PS V5以上。
Expand-Archive -Path C:\Users\Documents\UiPath\2\1.zip -DestinationPath C:\Users\Documents\UiPath\2

# 2. Windows内置解压
# 前提:需要.net 4.5以上
$BackUpPath = "C:\Users\Documents\UiPath\2\1.zip"
$Destination = "C:\Users\Documents\UiPath\2"
Add-Type -assembly "system.io.compression.filesystem"
[io.compression.zipfile]::ExtractToDirectory($BackUpPath, $destination)

