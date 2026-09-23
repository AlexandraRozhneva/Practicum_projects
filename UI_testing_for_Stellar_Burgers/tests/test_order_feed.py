import pytest
import allure
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage
import logging
import re

logger = logging.getLogger(__name__)


@allure.feature("Лента заказов")
class TestOrderFeed:
    
    @allure.story("Счетчики заказов")
    @allure.title("Счетчик 'Выполнено за всё время' увеличивается после создания заказа")
    def test_total_orders_counter_increases(self, driver, base_url, test_user_credentials):
        """Проверка увеличения счетчика 'Выполнено за всё время'"""
        driver.get(base_url)
        constructor_page = ConstructorPage(driver)
        
        logger.info(f"Регистрация пользователя: {test_user_credentials['email']}")
        constructor_page.register_user(
            test_user_credentials["email"],
            test_user_credentials["password"],
            test_user_credentials["name"]
        )
        
        logger.info(f"Авторизация пользователя: {test_user_credentials['email']}")
        constructor_page.login_user(
            test_user_credentials["email"], 
            test_user_credentials["password"]
        )
        
        constructor_page.click_order_feed()
        feed_page = OrderFeedPage(driver)
        
        initial_total_text = feed_page.get_total_orders_count()
        initial_total = int(initial_total_text) if initial_total_text.isdigit() else 0
        logger.info(f"Начальное значение счетчика 'Выполнено за всё время': {initial_total}")
        
        if initial_total == 0:
            logger.warning("Счетчик показывает 0, пробуем обновить страницу")
            driver.refresh()
            feed_page._wait_for_feed_load()
            initial_total_text = feed_page.get_total_orders_count()
            initial_total = int(initial_total_text) if initial_total_text.isdigit() else 0
            logger.info(f"Начальное значение после обновления: {initial_total}")
        
        feed_page.click_constructor()
        constructor_page.create_order()
        
        order_number = constructor_page.get_order_number()
        assert order_number, "Номер заказа не получен"
        logger.info(f"Создан заказ с номером: {order_number}")
        
        constructor_page.close_order_modal()
        constructor_page.click_order_feed()
        
        # Создаем WebDriverWait с увеличенным таймаутом для проверки счетчика
        from selenium.webdriver.support.ui import WebDriverWait
        wait = WebDriverWait(driver, 60)
        
        def total_updated(driver):
            current_text = feed_page.get_total_orders_count()
            current = int(current_text) if current_text.isdigit() else 0
            logger.info(f"Текущее значение счетчика: {current}, начальное: {initial_total}")
            return current > initial_total
        
        wait.until(total_updated)
        
        final_text = feed_page.get_total_orders_count()
        final_total = int(final_text) if final_text.isdigit() else 0
        
        assert final_total > initial_total, f"Счетчик не обновился. Начальное: {initial_total}, текущее: {final_total}"
        logger.info(f"Новое значение счетчика 'Выполнено за всё время': {final_total}")
    
    @allure.story("Счетчики заказов")
    @allure.title("Счетчик 'Выполнено за сегодня' увеличивается после создания заказа")
    def test_today_orders_counter_increases(self, driver, base_url, test_user_credentials):
        """Проверка увеличения счетчика 'Выполнено за сегодня'"""
        driver.get(base_url)
        constructor_page = ConstructorPage(driver)
        
        logger.info(f"Регистрация пользователя: {test_user_credentials['email']}")
        constructor_page.register_user(
            test_user_credentials["email"],
            test_user_credentials["password"],
            test_user_credentials["name"]
        )
        
        logger.info(f"Авторизация пользователя: {test_user_credentials['email']}")
        constructor_page.login_user(
            test_user_credentials["email"], 
            test_user_credentials["password"]
        )
        
        constructor_page.click_order_feed()
        feed_page = OrderFeedPage(driver)
        
        initial_today_text = feed_page.get_today_orders_count()
        initial_today = int(initial_today_text) if initial_today_text.isdigit() else 0
        logger.info(f"Начальное значение счетчика 'Выполнено за сегодня': {initial_today}")
        
        if initial_today == 0:
            logger.warning("Счетчик показывает 0, пробуем обновить страницу")
            driver.refresh()
            feed_page._wait_for_feed_load()
            initial_today_text = feed_page.get_today_orders_count()
            initial_today = int(initial_today_text) if initial_today_text.isdigit() else 0
            logger.info(f"Начальное значение после обновления: {initial_today}")
        
        feed_page.click_constructor()
        constructor_page.create_order()
        
        order_number = constructor_page.get_order_number()
        assert order_number, "Номер заказа не получен"
        logger.info(f"Создан заказ с номером: {order_number}")
        
        constructor_page.close_order_modal()
        constructor_page.click_order_feed()
        
        # Создаем WebDriverWait с увеличенным таймаутом для проверки счетчика
        from selenium.webdriver.support.ui import WebDriverWait
        wait = WebDriverWait(driver, 60)
        
        def today_updated(driver):
            current_text = feed_page.get_today_orders_count()
            current = int(current_text) if current_text.isdigit() else 0
            logger.info(f"Текущее значение счетчика: {current}, начальное: {initial_today}")
            return current > initial_today
        
        wait.until(today_updated)
        
        final_text = feed_page.get_today_orders_count()
        final_today = int(final_text) if final_text.isdigit() else 0
        
        assert final_today > initial_today, f"Счетчик не обновился. Начальное: {initial_today}, текущее: {final_today}"
        logger.info(f"Новое значение счетчика 'Выполнено за сегодня': {final_today}")
    
    @allure.story("Заказы в работе")
    @allure.title("Номер заказа появляется в разделе 'В работе'")
    def test_order_number_appears_in_progress(self, driver, base_url, test_user_credentials):
        """Проверка появления номера заказа в разделе 'В работе'"""
        driver.get(base_url)
        constructor_page = ConstructorPage(driver)
        
        logger.info(f"Регистрация пользователя: {test_user_credentials['email']}")
        constructor_page.register_user(
            test_user_credentials["email"],
            test_user_credentials["password"],
            test_user_credentials["name"]
        )
        
        logger.info(f"Авторизация пользователя: {test_user_credentials['email']}")
        constructor_page.login_user(
            test_user_credentials["email"], 
            test_user_credentials["password"]
        )
        
        constructor_page.create_order()
        
        order_number = constructor_page.get_order_number()
        assert order_number, "Номер заказа не получен"
        logger.info(f"Создан заказ с номером: {order_number}")
        
        constructor_page.close_order_modal()
        constructor_page.click_order_feed()
        feed_page = OrderFeedPage(driver)
        
        # Увеличиваем таймаут для ожидания заказа в работе
        feed_page.wait_for_order_in_progress(order_number, timeout=90)
        
        orders_in_progress = feed_page.get_orders_in_progress()
        logger.info(f"Заказы в работе: {orders_in_progress}")
        
        order_clean = re.sub(r'\D', '', order_number)
        found = False
        
        order_with_zero = "0" + order_clean if len(order_clean) == 6 else order_clean
        
        for order in orders_in_progress:
            order_clean_current = re.sub(r'\D', '', order)
            if order_clean_current == order_clean or order_clean_current == order_with_zero:
                found = True
                break
        
        assert found, f"Заказ {order_number} не найден в работе"
        logger.info(f"Заказ {order_number} успешно найден в разделе 'В работе'")