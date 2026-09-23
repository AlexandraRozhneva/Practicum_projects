from selenium.webdriver.common.by import By

class MainPageLocators:
    """Локаторы главной страницы"""
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")
    
    ACTIVE_BUNS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and span[text()='Булки']]//parent::div[contains(@class, 'tab_tab_type_current__2BEPc')]")
    ACTIVE_SAUCES_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and span[text()='Соусы']]//parent::div[contains(@class, 'tab_tab_type_current__2BEPc')]")
    ACTIVE_FILLINGS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and span[text()='Начинки']]//parent::div[contains(@class, 'tab_tab_type_current__2BEPc')]")
    
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

class AuthPageLocators:
    """Локаторы страниц авторизации и регистрации"""
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")

class AccountPageLocators:
    """Локаторы личного кабинета"""
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")