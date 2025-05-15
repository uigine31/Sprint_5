from selenium import webdriver

driver = webdriver.Edge()
driver.maximize_window()

# Открой страницу тестового стенда
driver.get('https://qa-mesto.praktikum-services.ru/')

# Проверь, что в url добавился /signin
assert '/signin' in driver.current_url

# Закрой браузер
driver.quit()
