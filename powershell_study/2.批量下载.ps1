# 下载单个文件
function DownloadItem {
    param([string]$url, [string]$path, [string]$filename , [string]$referer)
    if ($referer.Contains("(*)")) {
        $referer = $referer -replace "\(\*\)", $url
    }
    try {
        $tmpFileName = [System.IO.Path]::GetTempFileName()
        $destFileName = [System.IO.Path]::Combine($path, $filename)
        $watch = Measure-Command {
            # 下载文件到临时文件夹
            Invoke-WebRequest -Uri $url -Method Get -Headers @{"Referer" = $referer } -UserAgent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36" -TimeoutSec 120 -OutFile $tmpFileName
            # 将临时文件移动到目标文件夹
            Move-Item -Path $tmpFileName -Destination $destFileName -Force
        }
        $script:succeed += 1
        $fileLength = [Math]::Ceiling((Get-Item -LiteralPath $destFileName).Length / 1024.0)
        $elapsed = [Math]::Round($watch.TotalMilliseconds)
        # 下载成功！12.jpg - 115KB/2356ms
        Write-Host "下载成功！$filename - $fileLength KB/$elapsed ms" -ForegroundColor Green
    }
    catch {
        Write-Error $PSItem.ToString()
    }
    finally {
        $script:completed += 1
    }
}
$url = "https://qzrobot.top/index.php/s/y85HnHAHj8XPjCC/download"
$tmpFileName = "c:/temp/"
DownloadItem -url $url -path $tmpFileName -filename "asdf.xlsx"
#Invoke-WebRequest -Uri $url  -Method Get -Headers @{"Referer" = $referer } -UserAgent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36" -TimeoutSec 120 -OutFile $tmpFileName

# [int]$script:completed = 0  # 下载完成数量
# [int]$script:succeed = 0    # 下载成功数量

# # 开始下载（普通方法）
# function StartDownload {
#     param([array]$urlList, [string]$path, [string]$referer)
#     $last = $urlList.Count
#     $watch = Measure-Command {
#         for ($i = 0; $i -lt $last; $i++) {
#             DownloadItem -url $urlList[$i] -path $path -referer $referer
#             Start-Sleep -Milliseconds 200  # 延迟0.2秒
#         }
#     }
#     $failed = $script:completed - $succeed
#     $elapsed = [Math]::Round($watch.TotalMilliseconds / 1000, 2)  # 总计耗时（秒）
#     Write-Output ""
#     Write-Host "总共下载 $script:completed，成功 $script:succeed，失败 $failed，耗时 $elapsed s" -ForegroundColor Red -BackgroundColor Yellow
#     $script:completed = 0
#     $script:succeed = 0
# }



# # 主函数 运行 AppStart 即可启动
# function AppStart {
#     Clear-Host
#     Write-Welcome
#     $urlFormat = ReadInput_Url -message "输入URL(含通配符，例如 http://www.spany.com/2019/(*).jpg)"
#     $start = ReadInput_Integer -message "通配符数字开始(0~200)" -minValue 0 -maxValue 200
#     $end = $start + 200
#     $end = ReadInput_Integer -message "通配符数字结束($start~$end)" -minValue: $start -maxValue $end
#     $len = ReadInput_Integer -message "通配符数字长度(1~5)" -minValue: 1 -maxValue 5
#     $referer = ReadInput_Url -message "输入Referer为破解防盗链(如果Referer中含有通配符(*)，则将被当前URL替换，如无须Referer则直接回车)" -defaultValue "https://www.baidu.com/visit"
#     Write-Output ""

#     $urlList = BuildUrlList -urlFormat $urlFormat -start $start -end $end -len $len
#     if ($urlList.Count -gt 0) {
#         Write-Output "URL列表如下:"
#         foreach ($url in $urlList) {
#             Write-Output "`t$url"
#         }
#         Write-Output ""
#         if (ReadInput_YesOrNo -message "是否开始下载？(y/n)") {
#             $path = ReadInput_Path -message "输入文件存储路径(例如 E:\album\travel)"
#             Write-Output ""
#             StartDownload -urlList $urlList -path $path -referer $referer
#         }
#     }
#     else {
#         Write-Warning "不能创建URL列表，请核对参数！"
#     }
#     Write-Output ""
#     Write-Output "按任意键退出..."
#     [System.Console]::ReadKey($true) | Out-Null
# }

# AppStart