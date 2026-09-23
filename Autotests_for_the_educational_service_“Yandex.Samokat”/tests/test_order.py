import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.test_data import TestData
import logging

logger = logging.getLogger(__name__)

class TestOrder:
    """Тесты для оформления заказа"""
    
    @allure.title("Оформление заказа с верхней кнопкой")
    @allure.feature("Заказ самоката")
    @allure.story("Позитивный сценарий")
    @pytest.mark.parametrize("order_data", [TestData.ORDER_DATA[0], TestData.ORDER_DATA[1]])
    def test_order_with_top_button(self, driver, wait, order_data):
        """
        Проверка позитивного сценария заказа самоката через верхнюю кнопку
        """
        logger.info(f"=== ЗАПУСК ТЕСТА ЗАКАЗА (верхняя кнопка) ===")
        logger.info(f"Данные: {order_data['name']} {order_data['last_name']}")
        
        main_page = MainPage(driver, wait)
        main_page.open()
        main_page.close_cookie_banner()
        
        main_page.click_order_button_top()
        logger.info("Перешли на страницу заказа")
        
        order_page = OrderPage(driver, wait)
        success_message = order_page.complete_order(order_data)
        
        assert "Заказ оформлен" in success_message, \
            f"Сообщение об успехе не найдено. Получено: {success_message}"
        
        logger.info("=== ТЕСТ УСПЕШНО ЗАВЕРШЕН ===")
    
    @allure.title("Оформление заказа с нижней кнопкой")
    @allure.feature("Заказ самоката")
    @allure.story("Позитивный сценарий")
    @pytest.mark.parametrize("order_data", [TestData.ORDER_DATA[0], TestData.ORDER_DATA[1]])
    def test_order_with_bottom_button(self, driver, wait, order_data):
        """
        Проверка позитивного сценария заказа самоката через нижнюю кнопку
        """
        logger.info(f"=== ЗАПУСК ТЕСТА ЗАКАЗА (нижняя кнопка) ===")
        logger.info(f"Данные: {order_data['name']} {order_data['last_name']}")
        
        main_page = MainPage(driver, wait)
        main_page.open()
        main_page.close_cookie_banner()
        
        main_page.click_order_button_bottom()
        logger.info("Перешли на страницу заказа")
        
        order_page = OrderPage(driver, wait)
        success_message = order_page.complete_order(order_data)
        
        assert "Заказ оформлен" in success_message, \
            f"Сообщение об успехе не найдено. Получено: {success_message}"
        
        logger.info("=== ТЕСТ УСПЕШНО ЗАВЕРШЕН ===")