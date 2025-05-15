import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from urls import Urls

class TestProfileNavigation:
    def test_personal_account_transition(self, driver):
        driver.get(Urls.BASE_URL)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 20).until(EC.url_contains("login"))
        assert "login" in driver.current_url