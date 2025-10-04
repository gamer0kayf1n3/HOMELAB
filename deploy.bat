REM deploy.bat - safer deployment script for HomeServer

REM set log file
set LOGFILE=%~dp0deploy.log

echo [%date% %time%] Starting deployment... >> %LOGFILE%

timeout /t 3 > nul

REM stop service
echo Stopping HomeServer... >> %LOGFILE%
nssm stop HomeServer
if %ERRORLEVEL% neq 0 (
    echo Failed to stop HomeServer >> %LOGFILE%
    exit /b 1
)

REM switch to production branch
echo Checking out production branch... >> %LOGFILE%
git checkout production >> %LOGFILE% 2>&1
if %ERRORLEVEL% neq 0 (
    echo Failed to checkout production >> %LOGFILE%
    exit /b 1
)

REM pull latest code
echo Pulling latest changes... >> %LOGFILE%
git pull origin production >> %LOGFILE% 2>&1
if %ERRORLEVEL% neq 0 (
    echo Git pull failed >> %LOGFILE%
    exit /b 1
)

REM start service
echo Starting HomeServer... >> %LOGFILE%
nssm start HomeServer
if %ERRORLEVEL% neq 0 (
    echo Failed to start HomeServer >> %LOGFILE%
    exit /b 1
)

echo [%date% %time%] Deployment finished successfully! >> %LOGFILE%
echo Deployment finished!
