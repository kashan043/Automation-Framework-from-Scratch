import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")

    driver.implicitly_wait(15)
    driver.set_page_load_timeout(30)
    return driver

def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

<<<<<<< HEAD
# It is hook for Adding Environment info to HTML Report
# Hook to add environment info to HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_html_environment(config):
    return {
        "Project Name": "nop Commerce",
        "Module Name": "Customers",
        "Tester": "Kashan"
    }
>>>>>>> 236d73f (updating structure)

# Hook to delete/modify metadata (optional)
pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
