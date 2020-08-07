# ���ص����ļ�
function DownloadItem {
    param([string]$url, [string]$path, [string]$filename , [string]$referer)
    if ($referer.Contains("(*)")) {
        $referer = $referer -replace "\(\*\)", $url
    }
    try {
        $tmpFileName = [System.IO.Path]::GetTempFileName()
        $destFileName = [System.IO.Path]::Combine($path, $filename)
        $watch = Measure-Command {
            # �����ļ�����ʱ�ļ���
            Invoke-WebRequest -Uri $url -Method Get -Headers @{"Referer" = $referer } -UserAgent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36" -TimeoutSec 120 -OutFile $tmpFileName
            # ����ʱ�ļ��ƶ���Ŀ���ļ���
            Move-Item -Path $tmpFileName -Destination $destFileName -Force
        }
        $script:succeed += 1
        $fileLength = [Math]::Ceiling((Get-Item -LiteralPath $destFileName).Length / 1024.0)
        $elapsed = [Math]::Round($watch.TotalMilliseconds)
        # ���سɹ���12.jpg - 115KB/2356ms
        Write-Host "���سɹ���$filename - $fileLength KB/$elapsed ms" -ForegroundColor Green
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

# [int]$script:completed = 0  # �����������
# [int]$script:succeed = 0    # ���سɹ�����

# # ��ʼ���أ���ͨ������
# function StartDownload {
#     param([array]$urlList, [string]$path, [string]$referer)
#     $last = $urlList.Count
#     $watch = Measure-Command {
#         for ($i = 0; $i -lt $last; $i++) {
#             DownloadItem -url $urlList[$i] -path $path -referer $referer
#             Start-Sleep -Milliseconds 200  # �ӳ�0.2��
#         }
#     }
#     $failed = $script:completed - $succeed
#     $elapsed = [Math]::Round($watch.TotalMilliseconds / 1000, 2)  # �ܼƺ�ʱ���룩
#     Write-Output ""
#     Write-Host "�ܹ����� $script:completed���ɹ� $script:succeed��ʧ�� $failed����ʱ $elapsed s" -ForegroundColor Red -BackgroundColor Yellow
#     $script:completed = 0
#     $script:succeed = 0
# }



# # ������ ���� AppStart ��������
# function AppStart {
#     Clear-Host
#     Write-Welcome
#     $urlFormat = ReadInput_Url -message "����URL(��ͨ��������� http://www.spany.com/2019/(*).jpg)"
#     $start = ReadInput_Integer -message "ͨ������ֿ�ʼ(0~200)" -minValue 0 -maxValue 200
#     $end = $start + 200
#     $end = ReadInput_Integer -message "ͨ������ֽ���($start~$end)" -minValue: $start -maxValue $end
#     $len = ReadInput_Integer -message "ͨ������ֳ���(1~5)" -minValue: 1 -maxValue 5
#     $referer = ReadInput_Url -message "����RefererΪ�ƽ������(���Referer�к���ͨ���(*)���򽫱���ǰURL�滻��������Referer��ֱ�ӻس�)" -defaultValue "https://www.baidu.com/visit"
#     Write-Output ""

#     $urlList = BuildUrlList -urlFormat $urlFormat -start $start -end $end -len $len
#     if ($urlList.Count -gt 0) {
#         Write-Output "URL�б�����:"
#         foreach ($url in $urlList) {
#             Write-Output "`t$url"
#         }
#         Write-Output ""
#         if (ReadInput_YesOrNo -message "�Ƿ�ʼ���أ�(y/n)") {
#             $path = ReadInput_Path -message "�����ļ��洢·��(���� E:\album\travel)"
#             Write-Output ""
#             StartDownload -urlList $urlList -path $path -referer $referer
#         }
#     }
#     else {
#         Write-Warning "���ܴ���URL�б���˶Բ�����"
#     }
#     Write-Output ""
#     Write-Output "��������˳�..."
#     [System.Console]::ReadKey($true) | Out-Null
# }

# AppStart