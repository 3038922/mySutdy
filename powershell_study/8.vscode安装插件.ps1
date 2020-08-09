# Write-Host  "正在安装vscode插件sync" -ForegroundColor Green
# & code --install-extension shan.code-settings-sync

# "sync.gist": "6c091a7b4ddcb213e72d430dac23422f",

$newfile = @();
Get-Content C:\Users\$env:UserName\AppData\Roaming\Code\User\settings.json | #读取文件
% {
    $newfile += $_;
    if ($_ -like '{') {
        #找到匹配的字符串
        $newfile += '  "sync.gist": "6c091a7b4ddcb213e72d430dac23422f",' #加入新的行
    }
}
$newfile | Out-File test.json #输出