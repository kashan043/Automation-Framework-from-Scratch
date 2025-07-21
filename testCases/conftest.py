import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--headless")  # Optional for GitHub Actions
        chrome_options.add_argument("--remote-debugging-port=9222")  # Optional
        chrome_options.add_argument("--user-data-dir=/tmp/unique-profile")  # ✅ Unique temp dir
        driver = webdriver.Chrome(options=chrome_options)
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
