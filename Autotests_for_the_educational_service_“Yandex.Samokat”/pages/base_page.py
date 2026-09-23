import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

logger = logging.getLogger(__name__)

class BasePage:
    """Базовый класс для всех страниц с общими методами"""
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    
    @allure.step("Клик по элементу")
    def click_element(self, locator):
        """Клик по элементу с использованием JavaScript"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].click();", element)
            logger.info("Клик по элементу выполнен")
        except TimeoutException:
            logger.error(f"Элемент не кликабелен: {locator}")
            raise
    
    @allure.step("Ожидание видимости элемента")
    def wait_for_element_visible(self, locator):
        """Ожидание видимости элемента"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            logger.info("Элемент видим")
            return element
        except TimeoutException:
            logger.error(f"Элемент не появился: {locator}")
            raise
    
    @allure.step("Ожидание присутствия элемента в DOM")
    def wait_for_element_present(self, locator):
        """Ожидание присутствия элемента в DOM"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            logger.info("Элемент присутствует в DOM")
            return element
        except TimeoutException:
            logger.error(f"Элемент не найден в DOM: {locator}")
            raise
    
    @allure.step("Поиск элемента")
    def find_element(self, locator):
        """Поиск элемента"""
        return self.driver.find_element(*locator)
    
    @allure.step("Поиск всех элементов")
    def find_elements(self, locator):
        """Поиск всех элементов"""
        return self.driver.find_elements(*locator)
    
    @allure.step("Ввод текста в поле")
    def send_keys(self, locator, text):
        """Ввод текста в поле"""
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)
        logger.info(f"Введен текст: {text[:50]}")
    
    @allure.step("Получение текста элемента")
    def get_text(self, locator):
        """Получение текста элемента"""
        element = self.wait_for_element_visible(locator)
        text = element.text
        logger.info(f"Получен текст: {text[:50]}")
        return text
    
    @allure.step("Прокрутка к элементу")
    def scroll_to_element(self, locator):
        """Прокрутка до элемента"""
        element = self.wait_for_element_present(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        logger.info("Прокрутка к элементу выполнена")
        return element
    
    @allure.step("Ожидание загрузки JavaScript")
    def wait_for_js_ready(self):
        """Ожидание загрузки динамического контента через JavaScript"""
        try:
            self.wait.until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            logger.info("Страница полностью загружена")
        except TimeoutException:
            logger.warning("Таймаут ожидания загрузки JavaScript")
    
    @allure.step("Получение текущего URL")
    def get_current_url(self):
        """Получение текущего URL"""
        return self.driver.current_url
    
    @allure.step("Получение текущего окна")
    def get_current_window_handle(self):
        """Получение текущего окна"""
        return self.driver.current_window_handle
    
    @allure.step("Получение всех окон")
    def get_window_handles(self):
        """Получение списка всех открытых окон"""
        return self.driver.window_handles
    
    @allure.step("Переключение на новое окно")
    def switch_to_new_window(self, original_window_handle):
        """Переключение на новое окно"""
        self.wait.until(lambda d: len(d.window_handles) > 1)
        
        all_windows = self.get_window_handles()
        for window in all_windows:
            if window != original_window_handle:
                self.switch_to_window(window)
                logger.info("Переключено на новое окно")
                return window
        
        raise Exception("Новое окно не найдено")
    
    @allure.step("Переключение на окно")
    def switch_to_window(self, window_handle):
        """Переключение на указанное окно"""
        self.driver.switch_to.window(window_handle)
        logger.info(f"Переключено на окно: {window_handle}")
    
    @allure.step("Ожидание загрузки URL в новом окне")
    def wait_for_url_contains(self, text, timeout=20):
        """Ожидание, что URL содержит указанный текст"""
        self.wait.until(lambda d: text in d.current_url)
        logger.info(f"URL содержит: {text}")
    
    @allure.step("Закрытие текущего окна")
    def close_current_window(self):
        """Закрытие текущего окна"""
        self.driver.close()
        logger.info("Текущее окно закрыто")