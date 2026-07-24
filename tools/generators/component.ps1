param([string]$Name)

Write-Host ""
Write-Host "Generating component..." -ForegroundColor Cyan
Write-Host $Name -ForegroundColor Yellow

$component = Join-Path "frontend/src/components" $Name

if (Test-Path $component) {

    Write-Host ""
    Write-Host "⚠ Component '$Name' already exists." -ForegroundColor Yellow
    return

}

New-Item -ItemType Directory -Force -Path $component | Out-Null

& "$PSScriptRoot/../commands/Copy-Template.ps1" `
    "templates/component/Component.tsx.template" `
    "$component/$Name.tsx" `
    $Name

& "$PSScriptRoot/../commands/Copy-Template.ps1" `
    "templates/component/Component.module.css.template" `
    "$component/$Name.module.css" `
    $Name

& "$PSScriptRoot/../commands/Copy-Template.ps1" `
    "templates/component/Component.test.tsx.template" `
    "$component/$Name.test.tsx" `
    $Name

& "$PSScriptRoot/../commands/Copy-Template.ps1" `
    "templates/component/index.ts.template" `
    "$component/index.ts" `
    $Name

& "$PSScriptRoot/../commands/Copy-Template.ps1" `
    "templates/component/README.md.template" `
    "$component/README.md" `
    $Name

Write-Host ""
Write-Host "✅ Component generated:" -ForegroundColor Green
Write-Host $component