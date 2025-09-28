**Selenium Hybrid Framework (Python)**
This project is a Hybrid Test Automation Framework built with Python, Selenium, PyTest, and Page Object Model (POM).
It supports cross-browser testing, parallel execution, data-driven testing, logging and reporting.

**Features**
Page Object Model (POM) for maintainable test cases
Cross-browser testing (Chrome, Firefox, etc.)
Parallel execution with pytest-xdist
Data-driven testing using Excel (OpenPyXL)
Custom logging support
Automatic screenshots on failures
HTML and Allure reports
Easy scalability for adding new test cases

**Project Structure**
Selenium_Hybrid_Framework
│
├─ pageObjects/        # Page Object classes
├─ testCases/          # Test case scripts
├─ utilities/          # Utilities (Excel, Logger, Config reader)
├─ TestData/           # Excel test data
├─ Configurations/     # Config.ini file for environment setup
├─ Logs/               # Log files
├─ Screenshots/        # Captured screenshots on failures
├─ Reports/            # HTML/Allure reports
└─ Run.bat             # Batch file to trigger tests

**How TO Run Tests ?**
**Run on Chrome**
pytest -s -v testCases/test_login.py --browser chrome

**Run on Firefox**
pytest -s -v testCases/test_login.py --browser firefox

**Run Tests in Parallel** (3 threads)
pytest -s -v -n=3 testCases/test_login.py --browser chrome


**Author**
Ahmad Khan
