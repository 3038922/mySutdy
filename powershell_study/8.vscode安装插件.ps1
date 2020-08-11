

# "sync.gist": "6c091a7b4ddcb213e72d430dac23422f",
# C:\Users\$env:UserName\AppData\Roaming\Code\User\settings.json
# $json = ConvertFrom-Json($json)
# $json = ConvertFrom-Json( Get-Content( .\in.json -Encoding UTF8 ))
# # $json = ConvertFrom-Json -InputObject $json
# # $json | add-member -Name "sync.gist" -value "1234aaa" -MemberType NoteProperty -force
# write-host (ConvertTo-Json $json)
# $json = Get-Content -path .\in.json -Encoding UTF8 

$json = Get-Content C:\Users\$env:UserName\AppData\Roaming\Code\User\settings.json -Encoding UTF8 
# 注意换行
$json[0] += '
  "sync.gist": "6c091a7b4ddcb213e72d430dac23422f",'
Set-Content .\test.json -value $json -Encoding UTF8

# $settingsPath = ".\in.json";
# $colorSetting = 'workbench.colorTheme';
# $fontSetting = 'editor.fontSize';

# $data = Get-Content -Raw -Path $settingsPath -ErrorAction silentlycontinue | ConvertFrom-Json

# if ($data) {
#     $data | add-member -Name "sync.gist" -value "1234aaa" -MemberType NoteProperty -force
# }

# $data | ConvertTo-Json | Out-File $settingsPath -Encoding utf8