import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
import logging
import os

# Создание директории для логов, если её нет
os.makedirs('logs', exist_ok=True)

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/test.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def pytest_addoption(parser):
    """Добавление опций командной строки"""
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Запуск браузера в headless режиме"
    )
    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        help="Выбор браузера: firefox (по умолчанию)"
    )
    parser.addoption(
        "--geckodriver",
        action="store",
        default=None,
        help="Путь к geckodriver"
    )

@pytest.fixture(scope="function")
def driver(request):
    """Фикстура для создания и закрытия драйвера Firefox"""
    logger.info("Запуск теста в браузере Mozilla Firefox")
    
    options = FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    
    # Проверка headless режима
    if request.config.getoption("--headless"):
        options.add_argument("--headless")
        logger.info("Запуск в headless режиме")
    
    # Создание сервиса
    geckodriver_path = request.config.getoption("--geckodriver")
    if geckodriver_path and os.path.exists(geckodriver_path):
        service = FirefoxService(executable_path=geckodriver_path)
        logger.info(f"Используется geckodriver: {geckodriver_path}")
    else:
        service = FirefoxService()
        logger.info("Используется geckodriver из системного PATH")
    
    driver = webdriver.Firefox(service=service, options=options)
    driver.implicitly_wait(5)
    driver.set_page_load_timeout(30)
    
    yield driver
    
    driver.quit()
    logger.info("Драйвер закрыт")

@pytest.fixture(scope="function")
def wait(driver):
    """Фикстура для WebDriverWait с увеличенным таймаутом"""
    return WebDriverWait(driver, 20)