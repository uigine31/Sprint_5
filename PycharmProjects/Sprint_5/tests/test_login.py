import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators

class TestLogin:
    def test_login_main_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("evgsmoloviy22007@yandex.ru")
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 20).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("evgsmoloviy22007@yandex.ru")
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 20).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_from_registration_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("evgsmoloviy22007@yandex.ru")
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 20).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_from_recovery_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(*Locators.LOGIN_BUTTON_RECOVERY).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("evgsmoloviy22007@yandex.ru")
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 20).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"