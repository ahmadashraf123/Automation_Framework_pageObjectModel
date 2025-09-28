import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Command-line option
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests: chrome or firefox")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# Browser setup
@pytest.fixture
def setup(browser):
    options = None
    service = None
    driver = None

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    driver.maximize_window()
    yield driver
    driver.quit()


############  pytest HTML Reports #################

def pytest_configure(config):
    # pytest-metadata >= 3.0
    try:
        used_browser = config.getoption("--browser")
        from pytest_metadata.plugin import metadata_key
        config.stash[metadata_key]['Project Name'] = 'nopCommerce'
        config.stash[metadata_key]['Browser'] = used_browser  # was 'Chrome'
        config.stash[metadata_key]['Tester'] = 'Ahmad'
        return
    except Exception:
        pass
