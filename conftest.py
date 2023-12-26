import pytest
from selene import browser
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--category', action='store', default='скейтбординг',
                     help="Choose products category.")
    parser.addoption('--product', action='store', default='деки скейтовые',
                     help="Choose product type.")
    parser.addoption('--sort', action='store', default='сначала дешевое',
                     help="Choose products sort type.")

@pytest.fixture(scope="session", autouse=True)
def open_browser():
    driver = webdriver.Firefox()
    browser.config.driver = driver
    browser.config.base_url = 'https://www.skvot.com/'
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    yield
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