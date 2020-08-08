# 多条件判断
$ccls = Test-Path C:\ccls
if ($ccls) {
    Write-Host "ccls: $ccls" -ForegroundColor Green
    Remove-Item C:\ccls\ -recurse -force
}

$ninja = Test-Path C:\ninja
if ($ninja) {
    Write-Host "ninja: $ninja" -ForegroundColor Green
    Remove-Item C:\ninja\ -recurse -force
}
$llvm = Test-Path C:\llvm
if ($llvm) {
    Write-Host "llvm: $llvm" -ForegroundColor Green
    Remove-Item C:\llvm\ -recurse -force
}
$pros = Test-Path 'C:\Program Files\PROS'
if ($pros) {
    Write-Host "pros: $pros" -ForegroundColor Green
    Remove-Item -path 'C:\Program Files\PROS\' -recurse -force
}
$flag3 = -not $ccls -and -not $ninja -and -not $llvm
Write-Host $flag3 -ForegroundColor Green