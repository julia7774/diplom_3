import pytest
from selenium import webdriver

from pages.login import LoginPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser_name = request.param
    if browser_name == 'chrome':        
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox() 
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def authenticated(driver: webdriver.Chrome):
    page = LoginPage(driver)
    page.open()
    page.authenticate()
    return driver
