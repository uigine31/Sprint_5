from selenium.webdriver.common.by import By

class Locators:
    # Локатор для поля "Имя" 
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input[@class='text input__textfield text_type_main-default']")

    # Локатор для поля "Email" 
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input[@class='text input__textfield text_type_main-default']")

    # Локатор для поля "Пароль" 
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input[@class='text input__textfield text_type_main-default']")

    # Локатор для кнопки "Зарегистрироваться"
    SUBMIT_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")

    # Локатор для сообщения об ошибке пароля
    PASSWORD_ERROR = (By.XPATH, "//p[@class='input__error text_type_main-default']")

    # Локатор для сообщения об успешной регистрации
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='Auth_login__3hAey']")

    # Локатор для поля "Email" в окне входа
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")

    # Локатор для поля "Пароль" в окне входа
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")

    # Локатор для кнопки "Войти" в окне входа
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")

    # Локатор для кнопки "Войти в аккаунт" на главной странице
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")

    # Локатор для кнопки "Личный кабинет" на главной странице
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']")

    # Локатор для кнопки "Войти" в форме регистрации
    LOGIN_BUTTON_REGISTRATION = (By.XPATH, "//a[@class='Auth_link__1fOlj']")

    # Локатор для кнопки "Войти" в форме восстановления пароля
    LOGIN_BUTTON_RECOVERY = (By.XPATH, "//a[@class='Auth_link__1fOlj']")

    # Локатор для кнопки Булки
    BUNS_SECTION_BUTTON = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'and text()='Булки']")
    # Локатор для кнопки Соусы
    SAUCES_SECTION_BUTTON = (By.XPATH, "//span[@class='text text_type_main-default'and text()='Соусы']")
    # Локатор для кнопки Начинки
    FILLINGS_SECTION_BUTTON = (By.XPATH, "//span[@class='text text_type_main-default'and text()='Начинки']")

    # Локатор для заголовка Булки
    BUNS_SECTION_HEADER = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'and text()='Булки']")
    # Локатор для заголовка Соусы
    SAUCES_SECTION_HEADER = (By.XPATH, "//span[@class='text text_type_main-default'and text()='Соусы']")
    # Локатор для заголовка Начинки
    FILLINGS_SECTION_HEADER = (By.XPATH, "//span[@class='text text_type_main-default'and text()='Начинки']")

    # Локатор для кнопки "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']")

    # Локатор для логотипа "Stellar Burgers"
    LOGO_BUTTON = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")

    # Локатор для кнопки "Выход"
    SIGN_OUT_BUTTON = (By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive' and text()='Выход']")