import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators

class TestLogout:
    def test_logout(self, driver, login):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.SIGN_OUT_BUTTON))
        driver.find_element(*Locators.SIGN_OUT_BUTTON).click()
        WebDriverWait(driver, 20).until(EC.url_contains("login"))
        assert "login" in driver.current_url