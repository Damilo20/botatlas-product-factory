param(
    [string]$Command,
    [string]$Type,
    [string]$Name
)

switch ($Command) {

    "make" {

        switch ($Type) {

            "component" {

                $path = "frontend/src/components/$Name"
                & "$PSScriptRoot\generators\component.ps1" $Name

                New-Item -ItemType Directory -Force -Path $path | Out-Null

                New-Item -ItemType File -Force -Path "$path/$Name.tsx" | Out-Null

                Write-Host ""
                Write-Host "✅ Component created:"
                Write-Host $path
            }

            "page" {

                $path = "frontend/src/pages"

                New-Item -ItemType File -Force -Path "$path/$Name.tsx" | Out-Null

                Write-Host "✅ Page created."
            }

            "section" {

                $path = "frontend/src/sections"

                New-Item -ItemType File -Force -Path "$path/$Name.tsx" | Out-Null

                Write-Host "✅ Section created."
            }

            "feature" {

                $path = "frontend/src/features/$Name"

                mkdir $path -Force | Out-Null

                mkdir "$path/hooks" -Force | Out-Null
                mkdir "$path/services" -Force | Out-Null
                mkdir "$path/types" -Force | Out-Null

                New-Item -ItemType File -Force -Path "$path/index.ts" | Out-Null

                Write-Host "✅ Feature created."
            }

        }

    }

}