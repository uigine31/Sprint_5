from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://qa-mesto.praktikum-services.ru/")

# Найди кнопку и кликни по ней
driver.find_element(By.XPATH, ".//button[@class='auth-form__button']").click()

driver.quit()
