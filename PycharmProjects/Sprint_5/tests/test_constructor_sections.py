import pytest
from locators import Locators
from urls import Urls

class TestConstructorSections:
    def test_buns_section(self, driver):
        driver.get(Urls.BASE_URL)
        driver.find_element(*Locators.BUNS_SECTION_BUTTON).click()
        assert driver.find_element(*Locators.BUNS_SECTION_HEADER).is_displayed(), "Заголовок вкладки 'Булки' не отображается"

    def test_sauces_section(self, driver):
        driver.get(Urls.BASE_URL)
        driver.find_element(*Locators.SAUCES_SECTION_BUTTON).click()
        assert driver.find_element(*Locators.SAUCES_SECTION_HEADER).is_displayed(), "Заголовок вкладки 'Соусы' не отображается"

    def test_fillings_section(self, driver):
        driver.get(Urls.BASE_URL)
        driver.find_element(*Locators.FILLINGS_SECTION_BUTTON).click()
        assert driver.find_element(*Locators.FILLINGS_SECTION_HEADER).is_displayed(), "Заголовок вкладки 'Начинки' не отображается"