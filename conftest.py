import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def pytest_addoption(parser):
    parser.addoption("--url", action="store", help="Please enter application url")

@pytest.fixture
def driver():

    # Initialize ChromeDriver
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver_location = './helpers/chromedriver/chromedriver'
    os.chmod(driver_location, 0o775)
    driver = webdriver.Chrome(driver_location,options=chrome_options)
    
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()

@pytest.fixture()
def envurl(pytestconfig):
    return pytestconfig.getoption("url")