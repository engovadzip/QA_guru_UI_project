import os
import pytest
from dotenv import load_dotenv
from utils import attach
from selene import browser
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions

chrome_versions = ['99.0', '100.0']
firefox_versions = ['97.0', '98.0']


def pytest_addoption(parser):
    parser.addoption('--category', action='store', default='скейтбординг',
                     help="Choose products category.")
    parser.addoption('--product', action='store', default='деки скейтовые',
                     help="Choose product type.")
    parser.addoption('--sort', action='store', default='сначала дешевое',
                     help="Choose products sort type.")
    parser.addoption('--browser', action='store', default='chrome',
                     help="Choose browser name.")
    parser.addoption('--browser_version', action='store', default='100.0',
                     help="Choose browser version. For Chrome: 99.0 or 100.0. For Firefox: 97.0 or 98.0.")
    parser.addoption('--remote', action='store', default='off',
                     help="Remote mode: on or off.")
    parser.addoption('--search', action='store', default='volcom',
                     help="Search request.")


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    remote_mode = request.config.getoption("remote")
    browser_name = request.config.getoption("browser")
    browser_version = request.config.getoption('browser_version')

    browser.config.base_url = 'https://www.skvot.com/'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    if remote_mode.lower() == 'on':
        if browser_name.lower() == 'firefox':
            options = FirefoxOptions()
            if browser_version not in firefox_versions:
                raise pytest.UsageError("Choose one of the following versions: 97.0 or 98.0.")

        elif browser_name.lower() == 'chrome':
            options = ChromeOptions()
            if browser_version not in chrome_versions:
                raise pytest.UsageError("Choose one of the following versions: 99.0 or 100.0.")

        else:
            raise pytest.UsageError("Choose one of the following browsers: Chrome or Firefox.")

        selenoid_capabilities = {
            "browserName": browser_name.lower(),
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)

        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')

        driver = webdriver.Remote(command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
                                  options=options)
        browser.config.driver = driver

    elif remote_mode.lower() == 'off':
        if browser_name.lower() == 'firefox':
            driver = webdriver.Firefox()
            options = FirefoxOptions()
        elif browser_name.lower() == 'chrome':
            driver = webdriver.Chrome()
            options = ChromeOptions()

        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--incognito")
        browser.config.driver = driver

    else:
        raise pytest.UsageError('Choose "on" for remote launch of tests or choose "off" for local launch.')

    yield

    if browser_name.lower() == 'chrome':
        attach.add_html(browser)
        attach.add_logs(browser)

    if remote_mode.lower() == 'on':
        attach.add_video(browser)

    attach.add_screenshot(browser)

    browser.quit()


@pytest.fixture(scope='session')
def category(request):
    category = request.config.getoption("category")
    return category


@pytest.fixture(scope='session')
def product(request):
    product = request.config.getoption("product")
    return product


@pytest.fixture(scope='session')
def sort(request):
    sort = request.config.getoption("sort")
    return sort


@pytest.fixture(scope='session')
def search(request):
    search = request.config.getoption("search")
    return search
