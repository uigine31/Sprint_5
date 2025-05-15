from selenium import webdriver

driver = webdriver.Edge()
driver.maximize_window()
current_url = driver.current_url # полноэкранный режим

driver.get('https://qa-mesto.praktikum-services.ru/')

assert '/signin' in driver.current_url

