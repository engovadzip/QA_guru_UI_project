import pytest
from selene import browser
from selenium import webdriver



@pytest.fixture(scope="session", autouse=True)
def open_browser():
    driver = webdriver.Firefox()
    browser.config.driver = driver
    browser.config.base_url = 'https://www.skvot.com/'
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    yield
    browser.quit()