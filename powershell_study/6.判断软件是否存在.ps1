Write-Host "���ڼ��cmake�Ƿ�װ"  -ForegroundColor Green
$p = & { cmake --version } 2>&1
if ($p -is [System.Management.Automation.ErrorRecord]) {
    Write-Host "cmakeû�а�װ���߻�������û�����" -ForegroundColor Red
    Write-Host "�����򼴽�����,�밲װ���ٴγ���" -ForegroundColor Red
    return
}
else {
    Write-Host  $p -ForegroundColor Green
}
Write-Host "���ڼ��git�Ƿ�װ"  -ForegroundColor Green
$p = & { git --version } 2>&1
if ($p -is [System.Management.Automation.ErrorRecord]) {
    Write-Host "gitû�а�װ���߻�������û�����" -ForegroundColor Red
    Write-Host "�����򼴽�����,�밲װ���ٴγ���" -ForegroundColor Red
    return
}
else {
    Write-Host  $p -ForegroundColor Green
}
Write-Host "���ڼ��python�Ƿ�װ"  -ForegroundColor Green
$p = & { python --version } 2>&1
if ($p -is [System.Management.Automation.ErrorRecord]) {
    Write-Host "pythonû�а�װ���߻�������û�����" -ForegroundColor Red
    Write-Host "�����򼴽�����,�밲װ���ٴγ���" -ForegroundColor Red
    return
}
else {
    Write-Host  $p -ForegroundColor Green
}
Write-Host "���ڼ��vscode�Ƿ�װ"  -ForegroundColor Green
$p = & { code --version } 2>&1
if ($p -is [System.Management.Automation.ErrorRecord]) {
    Write-Host "vscodeû�а�װ���߻�������û�����" -ForegroundColor Red
    Write-Host "�����򼴽�����,�밲װ���ٴγ���" -ForegroundColor Red
    return
}
else {
    Write-Host  $p -ForegroundColor Green
}

# Write-Host "���ڼ��ninja�汾" -ForegroundColor Green
# $ninja = & ninja.exe --version
# Write-Host "���ڼ��clang�汾" -ForegroundColor Green
# $clang = & clang.exe --version
# Write-Host "���ڼ��ccls�汾" -ForegroundColor Green
# $ccls = & ccls.exe --version
# Write-Host "���ڼ��arm-none-eabi�汾" -ForegroundColor Green
# $arm_none_eabi = & arm-none-eabi-gcc.exe --version
# Write-Host "���ڼ��prosv5�汾" -ForegroundColor Green
# $prosv5 = & prosv5.exe --version
