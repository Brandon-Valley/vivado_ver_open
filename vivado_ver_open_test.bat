@echo off
set file_to_open_path=%1

set SCRIPT_PARENT_DIR=%~dp0

python %SCRIPT_PARENT_DIR%/src/main.py %file_to_open_path%



REM %VIVADO_BAT_PATH_2018_3% %file_to_open_path%