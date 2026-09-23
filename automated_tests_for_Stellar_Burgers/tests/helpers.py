from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import AuthPageLocators, MainPageLocators
from generators import generate_email, generate_password, generate_name
from selenium.webdriver.common.action_chains import ActionChains
import time

def create_driver():
    """Создает и настраивает драйвер браузера"""
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    return driver

def wait_and_find(driver, locator, timeout=15):
    """Ожидание элемента и его возврат"""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )

def wait_and_click(driver, locator, timeout=15):
    """Ожидание кликабельности элемента и клик"""
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    element.click()
    return element

def is_element_present(driver, locator, timeout=5):
    """Проверка наличия элемента"""
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return True
    except TimeoutException:
        return False

def register_user(driver):
    """Регистрирует нового пользователя и возвращает его данные"""
    email = generate_email()
    password = generate_password()
    name = generate_name()
    
    driver.get("https://stellarburgers.education-services.ru/register")
    
    wait_and_find(driver, AuthPageLocators.NAME_INPUT).send_keys(name)
    wait_and_find(driver, AuthPageLocators.EMAIL_INPUT).send_keys(email)
    wait_and_find(driver, AuthPageLocators.PASSWORD_INPUT).send_keys(password)
    wait_and_click(driver, AuthPageLocators.REGISTER_BUTTON)
    
    # Ждем перенаправления на страницу входа
    WebDriverWait(driver, 10).until(
        EC.url_contains("login")
    )
    
    return {"email": email, "password": password, "name": name}

def login_user(driver, email, password):
    """Выполняет вход пользователя"""
    wait_and_find(driver, AuthPageLocators.EMAIL_INPUT).send_keys(email)
    wait_and_find(driver, AuthPageLocators.PASSWORD_INPUT).send_keys(password)
    wait_and_click(driver, AuthPageLocators.LOGIN_BUTTON)
    
    # Ждем загрузки главной страницы
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
    )

def register_and_login_user(driver):
    """Регистрирует и выполняет вход пользователя"""
    user = register_user(driver)
    
    # Вход после регистрации
    login_user(driver, user["email"], user["password"])
    
    return user


def scroll_to_element_center(driver, element):
    """Прокрутка страницы до элемента с центрированием"""
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
    time.sleep(0.5)

def safe_click(driver, locator, timeout=15):
    """Универсальный безопасный клик с несколькими попытками"""
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )
    
    # Способы клика в порядке приоритета
    click_methods = [
        lambda: element.click(),  # Обычный клик
        lambda: ActionChains(driver).move_to_element(element).click().perform(),  # ActionChains
        lambda: driver.execute_script("arguments[0].click();", element)  # JavaScript
    ]
    
    for i, method in enumerate(click_methods):
        try:
            # Прокручиваем к элементу перед каждой попыткой
            scroll_to_element_center(driver, element)
            method()
            return element
        except:
            if i == len(click_methods) - 1:  # Если это была последняя попытка
                raise
            continue