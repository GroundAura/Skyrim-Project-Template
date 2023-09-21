@echo off
cd ".."

del "build\ProjectName.zip"
cd "dist\ProjectName"
"C:\Program Files\7-Zip\7z" a -tzip "..\..\build\ProjectName.zip"
cd "..\.."

del "D:\Games\Bethesda\Elder Scrolls\Skyrim\MO2\downloads\ProjectName.zip"
del "D:\Games\Bethesda\Elder Scrolls\Skyrim\MO2\downloads\ProjectName.zip.meta"
copy "build\ProjectName.zip" "D:\Games\Bethesda\Elder Scrolls\Skyrim\MO2\downloads"
copy "build\ProjectName.zip.meta" "D:\Games\Bethesda\Elder Scrolls\Skyrim\MO2\downloads"

