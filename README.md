🔧 Automation Testing Framework — Python + Selenium + Pytest + POM
📌 Overview
This is a robust, scalable, and modular UI Automation Testing Framework built from scratch using:

Python – clean, readable scripting

Selenium WebDriver – browser automation

Pytest – test runner with powerful features (fixtures, markers, parametrization)

Page Object Model (POM) – structured and maintainable design pattern

The framework is designed to support data-driven testing, cross-browser execution, and easy integration with CI/CD tools like Jenkins.

Project/
├── testCases/         → Test scripts (Pytest format)
│   └── test_login.py
│   └── test_signup.py
│
├── pageObjects/       → POM files (locators + reusable methods)
│   └── LoginPage.py
│   └── SignupPage.py
│
├── utilities/         → Helpers like Excel, config, logger
│   └── ExcelUtils.py
│   └── readConfig.py
│   └── CustomLogs.py
│
├── TestData/          → External data (Excel files)
│   └── TestData.xlsx
│
├── Screenshots/       → Captures on test failure
│
├── Logs/              → automation.log (logging info)
│
├── conftest.py        → Pytest fixtures (driver, browser, reporting)
├── pytest.ini         → Pytest config
└── requirements.txt   → Dependencies


✅ Key Features
✅ Selenium WebDriver for browser automation

✅ Pytest fixtures for setup/teardown and cross-browser support

✅ POM Design Pattern for maintainability and reusability

✅ Data-driven testing using Excel (via openpyxl)

✅ Custom Logger for structured logs

✅ Screenshot capture on test failures

✅ Pytest-HTML reporting

✅ Browser choice via CLI: --browser chrome, firefox, edge

✅ Ready for CI/CD pipeline integration

🚀 How to Run

# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest -v -s --html=Reports/report.html --browser chrome

