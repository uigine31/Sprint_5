import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locators.locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from urls import Urls
from test_data.test_data import TestData

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.get(Urls.LOGIN_PAGE)
    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(TestData.EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(TestData.PASSWORD)
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    WebDriverWait(driver, 20).until(EC.url_to_be(Urls.BASE_URL))
    yield