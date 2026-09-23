import allure
import pytest
from pages.main_page import MainPage
import logging

logger = logging.getLogger(__name__)

class TestRedirects:
    """Тесты для проверки редиректов по логотипам"""
    
    @allure.title("Проверка редиректа по логотипу Самоката")
    @allure.feature("Навигация")
    @allure.story("Логотипы")
    def test_scooter_logo_redirect(self, driver, wait):
        """
        Проверка, что клик по логотипу Самоката ведет на главную страницу
        """
        main_page = MainPage(driver, wait)
        main_page.open()
        main_page.close_cookie_banner()
        
        # Переход на страницу заказа
        main_page.click_order_button_top()
        
        # Клик по логотипу Самоката
        main_page.click_scooter_logo()
        
        # Проверка URL через метод страницы
        current_url = main_page.get_current_url()
        assert "qa-scooter" in current_url, \
            f"Неверный URL после клика по логотипу Самоката: {current_url}"
    
    @allure.title("Проверка редиректа по логотипу Яндекса")
    @allure.feature("Навигация")
    @allure.story("Логотипы")
    def test_yandex_logo_redirect(self, driver, wait):
        """
        Проверка, что клик по логотипу Яндекса открывает Дзен в новом окне
        """
        main_page = MainPage(driver, wait)
        main_page.open()
        main_page.close_cookie_banner()
        
        # Получаем текущее окно через метод страницы
        original_window = main_page.get_current_window_handle()
        original_windows_count = len(main_page.get_window_handles())
        logger.info(f"Исходное количество окон: {original_windows_count}")
        
        # Клик по логотипу Яндекса
        main_page.click_yandex_logo()
        
        # Переключаемся на новое окно через метод страницы
        main_page.switch_to_new_window(original_window)
        
        # Ожидаем загрузки страницы в новом окне через метод страницы
        main_page.wait_for_url_contains("dzen.ru")
        
        # Проверяем URL нового окна через метод страницы
        current_url = main_page.get_current_url()
        logger.info(f"URL в новом окне: {current_url}")
        
        assert "dzen.ru" in current_url or "yandex" in current_url.lower(), \
            f"Неверный URL после клика по логотипу Яндекса: {current_url}"
        
        
