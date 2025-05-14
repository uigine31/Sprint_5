import pytest
from locators import Locators

class TestConstructorSections:
    def test_constructor_sections(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.BUNS_SECTION_BUTTON).click()
        assert driver.find_element(*Locators.BUNS_SECTION_HEADER).is_displayed()
        driver.find_element(*Locators.SAUCES_SECTION_BUTTON).click()
        assert driver.find_element(*Locators.SAUCES_SECTION_HEADER).is_displayed()
        driver.find_element(*Locators.FILLINGS_SECTION_BUTTON).click()
        assert driver.find_element(*Locators.FILLINGS_SECTION_HEADER).is_displayed()