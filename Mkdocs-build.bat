@echo off

REM Build the MkDocs site
mkdocs build
IF %ERRORLEVEL% NEQ 0 (
    echo MkDocs build failed!
    exit /b %ERRORLEVEL%
)

REM Change directory to the 'site' folder
cd site
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to change directory to 'site'!
    exit /b %ERRORLEVEL%
)

REM Open the 'site' folder in Explorer
explorer %cd%
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to open the 'site' folder in Explorer!
    exit /b %ERRORLEVEL%
)

echo Build and directory change successful!
