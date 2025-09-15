# ----------------------------
# Log Archiving Script (Windows)
# ----------------------------

# Source directory containing logs
$SourceDir = "C:\Logs\MyApp"

# Destination directory for archives
$DestDir = "C:\Logs\Archive"

# Ensure destination directory exists
If (!(Test-Path -Path $DestDir)) {
    New-Item -ItemType Directory -Path $DestDir
}

# Generate timestamp
$Timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"

# Archive filename
$ArchiveName = "Logs_$Timestamp.zip"
$ArchivePath = Join-Path $DestDir $ArchiveName

# Compress logs into ZIP file
Compress-Archive -Path "$SourceDir\*" -DestinationPath $ArchivePath -Force

# Check if compression succeeded
If (Test-Path $ArchivePath) {
    Write-Host "✅ Logs archived successfully: $ArchivePath"
} Else {
    Write-Host "❌ Error archiving logs!"
    Exit 1
}

# Optional: Delete original logs after archiving
# Remove-Item "$SourceDir\*" -Recurse -Force

# Maintain archive log
$LogFile = Join-Path $DestDir "archive_log.txt"
"$Timestamp : Archived logs to $ArchiveName" | Out-File -FilePath $LogFile -Append
