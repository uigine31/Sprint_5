import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locators
from helpers.data_helpers import generate_random_email, generate_random_password
from test_data.test_data import TestData
from urls import Urls

class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get(Urls.REGISTER_PAGE)
        driver.find_element(*Locators.NAME_INPUT).send_keys(TestData.NAME)
        email = generate_random_email()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        password = generate_random_password()
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 20).until(EC.url_to_be(Urls.LOGIN_PAGE))
        assert driver.current_url == Urls.LOGIN_PAGE

    def test_registration_existing_user(self, driver):
        driver.get(Urls.REGISTER_PAGE)
        driver.find_element(*Locators.NAME_INPUT).send_keys(TestData.NAME)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(TestData.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(TestData.PASSWORD)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()
        error_message = (By.XPATH, "//p[contains(text(), 'Такой пользователь уже существует')]")
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(error_message))
        assert driver.find_element(*error_message).is_displayed()

    def test_registration_invalid_password(self, driver):
        driver.get(Urls.REGISTER_PAGE)
        driver.find_element(*Locators.NAME_INPUT).send_keys(TestData.NAME)
        email = generate_random_email()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        password = generate_random_password(length=5)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()
        error = driver.find_element(*Locators.PASSWORD_ERROR)
        assert error.is_displayed()