@echo off

echo ===================================
echo    AKSHAY CUSTOMIZE TEST RUNNER 2
echo ===================================
echo.

if not exist reports mkdir reports
if not exist screenshots mkdir screenshots
if not exist logs mkdir logs
if not exist reports\allure-results mkdir reports\allure-results

REM Default execution
set TEST_TARGET=%1

if "%TEST_TARGET%"=="" (
    set TEST_TARGET=tests/test_dummy.py
)

echo Running: %TEST_TARGET%
echo.

pytest %TEST_TARGET% --alluredir=reports/allure-results

echo.
echo ==========================================
echo    TEST EXECUTION COMPLETED
echo ==========================================
echo.
pause