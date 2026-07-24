param(
    [string]$Template,
    [string]$Destination,
    [string]$Name
)

$content = Get-Content $Template -Raw

$content = $content.Replace("{{NAME}}", $Name)

$folder = Split-Path $Destination

if (!(Test-Path $folder)) {
    New-Item -ItemType Directory -Force -Path $folder | Out-Null
}

$content | Set-Content $Destination -Encoding UTF8