# QA Internship Assignment - Part 4: Selenium Automation

## Project Overview
This project contains automated tests for the Future Code Technologies internship application form using Selenium WebDriver and Python.

## Features Tested
- ✅ Successful application submission
- ❌ Invalid email validation
- 🐛 Invalid phone validation (BUG TEST)
- 🐛 Invalid name validation (BUG TEST)
- ❌ Empty required fields
- ❌ Invalid file type
- ❌ File size limit
- ✅ Real-time validation

## Project Structure
```
Selenium Automation/
├── tests/
│   ├── __init__.py
│   └── test_internship_application.py
├── pages/
│   ├── __init__.py
│   └── internship_application_page.py
├── utils/
│   ├── __init__.py
│   └── test_data.py
├── reports/
├── screenshots/
├── test_files/
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Install Python
Download and install Python from https://www.python.org/downloads/

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Tests
```bash
# Run all tests
pytest

# Run with HTML report
pytest --html=reports/report.html

# Run specific test
pytest tests/test_internship_application.py::TestInternshipApplication::test_successful_application_submission -v
```

## Test Results
- Screenshots are saved in the `screenshots/` folder
- HTML reports are generated in the `reports/` folder
- Test execution logs are displayed in the console

## Bugs Found
1. **Phone Number Validation Bypass**: Application accepts invalid phone numbers like "abc"
2. **Name Field Validation Bypass**: Application accepts special characters in names like "Rashini@123"

## Technologies Used
- Python 3.x
- Selenium WebDriver 4.15.0
- pytest 7.4.3
- Chrome WebDriver
- Page Object Model Pattern

## Author
QA Internship Assignment - Future Code Tech Stack
