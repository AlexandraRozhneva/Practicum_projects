from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import logging

logger = logging.getLogger(__name__)


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 30)
        self._actions = ActionChains(driver)
        self._logger = logger

    def find_element(self, locator):
        """Находит элемент с явным ожиданием"""
        try:
            return self._wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self._logger.error(f"Элемент не найден: {locator}")
            raise

    def find_elements(self, locator):
        """Находит все элементы с явным ожиданием"""
        try:
            self._wait.until(EC.presence_of_element_located(locator))
            return self._driver.find_elements(*locator)
        except TimeoutException:
            self._logger.error(f"Элементы не найдены: {locator}")
            return []

    def click_element(self, locator):
        """Кликает по элементу с ожиданием кликабельности"""
        element = self._wait.until(EC.element_to_be_clickable(locator))
        element.click()
        self._logger.info(f"Клик по элементу: {locator}")

    def click_element_by_js(self, locator):
        """Принудительный клик через JavaScript"""
        element = self.find_element(locator)
        self._driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self._driver.execute_script("arguments[0].click();", element)
        self._logger.info(f"Принудительный клик через JS по элементу: {locator}")

    def get_text(self, locator):
        """Получает текст элемента"""
        try:
            element = self.find_element(locator)
            return element.text
        except Exception as e:
            self._logger.error(f"Ошибка при получении текста: {e}")
            raise

    def is_element_visible(self, locator):
        """Проверяет, видим ли элемент"""
        try:
            element = self._wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except TimeoutException:
            return False

    def wait_for_element_disappear(self, locator):
        """Ожидает исчезновения элемента"""
        try:
            self._wait.until(EC.invisibility_of_element_located(locator))
            self._logger.info(f"Элемент исчез: {locator}")
        except TimeoutException:
            self._logger.warning(f"Элемент не исчез за отведенное время: {locator}")

    def drag_and_drop(self, source_locator, target_locator):
        """Выполняет drag-and-drop"""
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        self._actions.drag_and_drop(source, target).perform()
        self._logger.info(f"Drag-and-drop выполнен: {source_locator} -> {target_locator}")
        
    def wait_for_url_contains(self, text):
        """Ожидает, что URL содержит указанный текст"""
        self._wait.until(EC.url_contains(text))
    
    def scroll_to_element(self, locator):
        """Прокручивает страницу до элемента"""
        element = self.find_element(locator)
        self._driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def execute_script(self, script, *args):
        """Выполняет JavaScript скрипт"""
        return self._driver.execute_script(script, *args)
    
    def get(self, url):
        """Переходит по указанному URL"""
        self._driver.get(url)
        self._logger.info(f"Перешли по URL: {url}")
    
    def get_current_url(self):
        """Получает текущий URL"""
        return self._driver.current_url
    
    def refresh(self):
        """Обновляет страницу"""
        self._driver.refresh()
        self._logger.info("Страница обновлена")
    
    def wait_for_element(self, locator, timeout=30):
        """Ожидает появления элемента с указанным таймаутом"""
        wait = WebDriverWait(self._driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))
    
    def wait_for_condition(self, condition, timeout=30):
        """Ожидает выполнения условия с указанным таймаутом"""
        wait = WebDriverWait(self._driver, timeout)
        return wait.until(condition)
    
    def find_elements_by_xpath(self, xpath):
        """Находит элементы по XPath"""
        return self._driver.find_elements(By.XPATH, xpath)
    
    def get_capabilities(self):
        """Получает возможности браузера"""
        return self._driver.capabilities