import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from test_data.test_data import TestData
from urls import Urls

class TestLogin:
    def test_login_main_page(self, driver):
        driver.get(Urls.BASE_URL)
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(TestData.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(TestData.PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 20).until(EC.url_to_be(Urls.BASE_URL))
        assert driver.current_url == Urls.BASE_URL

    def test_login_personal_account(self, driver):
        driver.get(Urls.BASE_URL)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(TestData.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(TestData.PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 20).until(EC.url_to_be(Urls.BASE_URL))
        assert driver.current_url == Urls.BASE_URL

    def test_login_from_registration_form(self, driver):
        driver.get(Urls.REGISTER_PAGE)
        driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(TestData.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(TestData.PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 20).until(EC.url_to_be(Urls.BASE_URL))
        assert driver.current_url == Urls.BASE_URL

    def test_login_from_recovery_form(self, driver):
        driver.get(Urls.FORGOT_PASSWORD_PAGE)
        driver.find_element(*Locators.LOGIN_BUTTON_RECOVERY).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(TestData.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(TestData.PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 20).until(EC.url_to_be(Urls.BASE_URL))
        assert driver.current_url == Urls.BASE_URL