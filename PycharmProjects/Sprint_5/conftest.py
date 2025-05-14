import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locators.locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("evgsmoloviy22007@yandex.ru")
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    WebDriverWait(driver, 20).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
    yield