@echo off

echo ===================================
echo    AKSHAY CUSTOMIZE TEST RUNNER
echo ===================================
echo.

if not exist reports mkdir reports
if not exist screenshots mkdir screenshots
if not exist logs mkdir logs
if not exist reports\allure-results mkdir reports\allure-results

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
goto REPORT

:SANITY
echo.
echo Running SANITY tests...
pytest tests/ -m sanity
goto REPORT

:REGRESSION
echo.
echo Running REGRESSION tests...
pytest tests/ -m regression
goto REPORT

:SMOKE
echo.
echo Running SMOKE tests...
pytest tests/ -m smoke
goto REPORT

:LOGIN
echo.
echo Running LOGIN Data Driven tests...
pytest tests/test_google_sheet_driven_login.py
goto REPORT

:EXIT
echo Exiting...
exit /b

:REPORT
echo.
echo Generating Allure Report...
allure generate reports/allure-results --clean -o reports/allure-report
allure open reports/allure-report
goto END

:END
echo.
echo ==========================================
echo    TEST EXECUTION COMPLETED
echo ==========================================
echo.
echo Allure Report  → reports/allure-report/index.html
echo Logs           → logs/test_execution.log
echo Screenshots    → screenshots/
echo.
pause