Write-Host "正在检查cmake是否安装"  -ForegroundColor Green
$p = & { cmake --version } 2>&1
if ($p -is [System.Management.Automation.ErrorRecord]) {
    Write-Host "cmake没有安装或者环境变量没有添加" -ForegroundColor Red
    Write-Host "本程序即将结束,请安装后再次尝试" -ForegroundColor Red
    return
}
else {
    Write-Host  $p -ForegroundColor Green
}
Write-Host "正在检查git是否安装"  -ForegroundColor Green
$p = & { git --version } 2>&1
if ($p -is [System.Management.Automation.ErrorRecord]) {
    Write-Host "git没有安装或者环境变量没有添加" -ForegroundColor Red
    Write-Host "本程序即将结束,请安装后再次尝试" -ForegroundColor Red
    return
}
else {
    Write-Host  $p -ForegroundColor Green
}
Write-Host "正在检查python是否安装"  -ForegroundColor Green
$p = & { python --version } 2>&1
if ($p -is [System.Management.Automation.ErrorRecord]) {
    Write-Host "python没有安装或者环境变量没有添加" -ForegroundColor Red
    Write-Host "本程序即将结束,请安装后再次尝试" -ForegroundColor Red
    return
}
else {
    Write-Host  $p -ForegroundColor Green
}
Write-Host "正在检查vscode是否安装"  -ForegroundColor Green
$p = & { code --version } 2>&1
if ($p -is [System.Management.Automation.ErrorRecord]) {
    Write-Host "vscode没有安装或者环境变量没有添加" -ForegroundColor Red
    Write-Host "本程序即将结束,请安装后再次尝试" -ForegroundColor Red
    return
}
else {
    Write-Host  $p -ForegroundColor Green
}

# Write-Host "正在检查ninja版本" -ForegroundColor Green
# $ninja = & ninja.exe --version
# Write-Host "正在检查clang版本" -ForegroundColor Green
# $clang = & clang.exe --version
# Write-Host "正在检查ccls版本" -ForegroundColor Green
# $ccls = & ccls.exe --version
# Write-Host "正在检查arm-none-eabi版本" -ForegroundColor Green
# $arm_none_eabi = & arm-none-eabi-gcc.exe --version
# Write-Host "正在检查prosv5版本" -ForegroundColor Green
# $prosv5 = & prosv5.exe --version
