$destination = "C:\Combined"
mkdir $destination -Force

Get-ChildItem -Directory | ForEach-Object {
    $files = Get-ChildItem $_.FullName -File
    if ($files.Count -eq 1) {
        Move-Item $files.FullName -Destination $destination
    }
}
