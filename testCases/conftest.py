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
    else:
        raise ValueError("Browser not supported!")

    driver.implicitly_wait(15)
    driver.set_page_load_timeout(30)

    yield driver  # ✅ yield gives the driver to the test

    driver.quit()  # ✅ clean up after test

def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


# ✅ Hook to add environment info to HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_html_environment(config):
    return {
        "Project Name": "nop Commerce",
        "Module Name": "Customers",
        "Tester": "Kashan"
    }

# ✅ Hook to delete/modify metadata (optional)
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
