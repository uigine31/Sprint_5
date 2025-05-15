import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from urls import Urls

class TestConstructorNavigation:
    def test_from_account_to_constructor(self, driver, login):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 20).until(EC.url_to_be(Urls.BASE_URL))
        assert driver.current_url == Urls.BASE_URL

    def test_from_account_to_constructor_logo(self, driver, login):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.LOGO_BUTTON).click()
        WebDriverWait(driver, 20).until(EC.url_to_be(Urls.BASE_URL))
        assert driver.current_url == Urls.BASE_URL