@echo off
echo QA Internship Assignment - Part 4: Selenium Automation
echo Future Code Tech Stack
echo ================================================

echo.
echo Installing required packages...
pip install -r requirements.txt

echo.
echo Creating necessary directories...
if not exist "reports" mkdir reports
if not exist "screenshots" mkdir screenshots
if not exist "test_files" mkdir test_files

echo.
echo Running automated tests...
python -m pytest tests/test_internship_application.py --html=reports/report.html --self-contained-html -v

echo.
echo Test execution completed!
echo Check reports/report.html for detailed results
echo Check screenshots/ folder for test screenshots
pause
