import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import logging
from generators import generate_email, generate_password, generate_name

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption(
        "--browser", 
        action="store", 
        default="chrome", 
        help="Browser: chrome or firefox"
    )


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    logger.info(f"Запуск теста в браузере: {browser}")
    
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser}")
    
    driver.maximize_window()
    driver.implicitly_wait(0)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def base_url():
    """Фикстура с базовым URL"""
    return "https://stellarburgers.education-services.ru/"


@pytest.fixture(scope="function")
def test_user_credentials():
    """Фикстура с динамическими тестовыми данными пользователя"""
    return {
        "email": generate_email(),
        "password": generate_password(),
        "name": generate_name()
    }