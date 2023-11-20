@echo off
set VENV_DIR=env

REM Check if the virtual environment exists
if not exist %VENV_DIR%\Scripts\activate.bat (
    echo Creating Python virtual environment...
    python -m venv %VENV_DIR%
)

REM Activate the virtual environment
call %VENV_DIR%\Scripts\activate

REM Install or upgrade jisho_api
python -m pip install --upgrade jisho_api

echo Python virtual environment is ready with jisho_api installed.
echo To activate the environment, run: call %VENV_DIR%\Scripts\activate
