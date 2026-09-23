from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
import logging
import re

logger = logging.getLogger(__name__)


class OrderFeedPage(BasePage):
    # Локаторы навигации
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")
    
    # Локаторы счетчиков
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    TOTAL_ORDERS_COUNTER_ALT = (By.XPATH, "//p[contains(text(), 'за все время')]/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    TODAY_ORDERS_COUNTER_ALT = (By.XPATH, "//p[contains(text(), 'за сегодня')]/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    
    # Локатор для раздела "В работе"
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]//li[contains(@class, 'text_type_digits-default')]")
    ORDER_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]")

    @allure.step("Переход на конструктор")
    def click_constructor(self):
        """Переход на конструктор"""
        self.click_element_by_js(self.CONSTRUCTOR_BUTTON)

    @allure.step("Переход в ленту заказов")
    def click_order_feed(self):
        """Переход в ленту заказов"""
        self.click_element_by_js(self.ORDER_FEED_BUTTON)
        self._wait_for_feed_load()

    def _wait_for_feed_load(self):
        """Ожидание загрузки ленты заказов"""
        try:
            self._wait.until(EC.presence_of_element_located(self.ORDER_LIST))
            logger.info("Лента заказов загружена")
        except:
            logger.warning("Список заказов не найден, продолжаем выполнение")

    @allure.step("Получение счетчика 'Выполнено за всё время'")
    def get_total_orders_count(self):
        """Получение значения счетчика 'Выполнено за всё время'"""
        try:
            text = self.get_text(self.TOTAL_ORDERS_COUNTER)
            numbers = re.findall(r'\d+', text)
            return numbers[0] if numbers else "0"
        except:
            try:
                text = self.get_text(self.TOTAL_ORDERS_COUNTER_ALT)
                numbers = re.findall(r'\d+', text)
                return numbers[0] if numbers else "0"
            except Exception as e:
                logger.error(f"Ошибка при получении счетчика 'Выполнено за всё время': {e}")
                return "0"

    @allure.step("Получение счетчика 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        """Получение значения счетчика 'Выполнено за сегодня'"""
        try:
            text = self.get_text(self.TODAY_ORDERS_COUNTER)
            numbers = re.findall(r'\d+', text)
            return numbers[0] if numbers else "0"
        except:
            try:
                text = self.get_text(self.TODAY_ORDERS_COUNTER_ALT)
                numbers = re.findall(r'\d+', text)
                return numbers[0] if numbers else "0"
            except Exception as e:
                logger.error(f"Ошибка при получении счетчика 'Выполнено за сегодня': {e}")
                return "0"

    @allure.step("Получение заказов в работе")
    def get_orders_in_progress(self):
        """Получение списка заказов в работе"""
        try:
            elements = self.find_elements(self.ORDERS_IN_PROGRESS)
            orders = [el.text for el in elements if el.text.strip()]
            logger.info(f"Найдены заказы в работе: {orders}")
            return orders
        except Exception as e:
            logger.error(f"Ошибка при получении заказов в работе: {e}")
            return []

    @allure.step("Ожидание появления заказа в разделе 'В работе'")
    def wait_for_order_in_progress(self, expected_order_number, timeout=90):
        """Ожидание появления заказа в разделе 'В работе'"""
        logger.info(f"Ожидаем появления заказа {expected_order_number} в разделе 'В работе' (таймаут: {timeout} секунд)")
        
        expected_clean = re.sub(r'\D', '', expected_order_number)
        logger.info(f"Очищенный номер заказа: {expected_clean}")
        
        expected_with_zero = expected_clean
        if len(expected_clean) == 6:
            expected_with_zero = "0" + expected_clean
            logger.info(f"Вариант с ведущим нулем: {expected_with_zero}")
        
        # Создаем новый WebDriverWait с увеличенным таймаутом
        from selenium.webdriver.support.ui import WebDriverWait
        wait = WebDriverWait(self._driver, timeout)
        
        def order_in_progress(driver):
            orders = self.get_orders_in_progress()
            if orders:
                logger.info(f"Проверяем заказы: {orders}")
                for order in orders:
                    order_clean = re.sub(r'\D', '', order)
                    if order_clean == expected_clean or order_clean == expected_with_zero:
                        logger.info(f"Заказ {expected_order_number} найден в разделе 'В работе'")
                        return True
            return False
        
        wait.until(order_in_progress)
        logger.info(f"Заказ {expected_order_number} успешно найден в разделе 'В работе'")