@echo off

echo ===================================
echo    AKSHAY CUSTOMIZE TEST RUNNER
echo ===================================
echo.

if not exist reports mkdir reports
if not exist screenshots mkdir screenshots
if not exist logs mkdir logs

echo Select test suite to run:
echo.
echo [1] All Tests
echo [2] Sanity Tests
echo [3] Regression Tests
echo [4] Smoke Tests
echo [5] Login Google Sheet Data Driven Tests
echo [6] Exit
echo.

set /p choice=Enter choice (1-6):

if "%choice%"=="1" goto ALL
if "%choice%"=="2" goto SANITY
if "%choice%"=="3" goto REGRESSION
if "%choice%"=="4" goto SMOKE
if "%choice%"=="5" goto LOGIN
if "%choice%"=="6" goto EXIT

:ALL
echo.
echo Running ALL tests...
pytest tests/
goto END

:SANITY
echo.
echo Running SANITY tests...
pytest tests/ -m sanity
goto END

:REGRESSION
echo.
echo Running REGRESSION tests...
pytest tests/ -m regression
goto END

:SMOKE
echo.
echo Running SMOKE tests...
pytest tests/ -m smoke
goto END

:LOGIN
echo.
echo Running LOGIN Data Driven tests...
pytest tests/test_google_sheet_driven_login.py
goto END

:EXIT
echo Exiting...
exit /b

:END
echo.
echo ==========================================
echo    TEST EXECUTION COMPLETED
echo ==========================================
echo.
echo Reports      reports/report.html
echo Logs         logs/test_execution.log
echo Screenshots  screenshots/
echo.
pause