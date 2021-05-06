from selenium import webdriver
from Configurations.config import TestData

import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\\Users\\rajalaxmi.nayak\\Drivers\\chromedriver.exe")
    elif browser == 'Ie':
        driver = webdriver.Ie(executable_path="C:\\Users\\rajalaxmi.nayak\\Drivers\\IEDriverServer.exe")
    else:
        driver = webdriver.Firefox(executable_path="C:\\Users\\rajalaxmi.nayak\\Drivers\Firefoxdriver\\geckodriver.exe")
    return driver




def pytest_addoption(parser): # This will get the value from CLI
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #Thsi will return the browser value to setup method
    return  request.config.getoption("--browser")
