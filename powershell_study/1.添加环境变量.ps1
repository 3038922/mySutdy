# ����ȫ���޸�windows10ϵͳ��������
$path = [environment]::GetEnvironmentVariable('Path', 'machine') # ��ȡ����
$addPath = @('C:\Program Files\Git\cmd', 'c:\test', 'c:\windows')

foreach ($it in $addPath) { 
    if ($path.split(";") -Contains $it) {
        Write-Host "·��: $it �Ѵ���" -ForegroundColor yellow 
    }
    else {
        $path += ($it + ";")
        Write-Host "·��: $it �����" -ForegroundColor green 
    }
}
Write-Host "$path" -ForegroundColor Green

#[environment]::SetEnvironmentvariable("Path", $newvalue, "machine") #���û������� user machine