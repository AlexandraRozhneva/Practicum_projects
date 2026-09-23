import pytest
import allure
import logging
from pages.constructor_page import ConstructorPage

logger = logging.getLogger(__name__)


@allure.feature("Конструктор")
class TestConstructor:
    
    @allure.story("Навигация")
    @allure.title("Переход по клику на 'Конструктор'")
    def test_click_constructor(self, driver, base_url):
        """Проверка перехода на конструктор"""
        driver.get(base_url)
        page = ConstructorPage(driver)
        page.click_constructor()
        assert "constructor" in driver.current_url or driver.current_url == base_url
    
    @allure.story("Навигация")
    @allure.title("Переход по клику на 'Лента заказов'")
    def test_click_order_feed(self, driver, base_url):
        """Проверка перехода в ленту заказов"""
        driver.get(base_url)
        page = ConstructorPage(driver)
        page.click_order_feed()
        assert "feed" in driver.current_url
    
    @allure.story("Ингредиенты")
    @allure.title("Клик по ингредиенту открывает модальное окно с деталями")
    def test_ingredient_modal_appears(self, driver, base_url):
        """Проверка открытия модального окна при клике на ингредиент"""
        driver.get(base_url)
        page = ConstructorPage(driver)
        page.click_ingredient()
        assert page.is_modal_visible()
    
    @allure.story("Ингредиенты")
    @allure.title("Модальное окно закрывается кликом по крестику")
    def test_modal_closes_by_cross(self, driver, base_url):
        """Проверка закрытия модального окна"""
        driver.get(base_url)
        page = ConstructorPage(driver)
        page.click_ingredient()
        assert page.is_modal_visible()
        page.close_modal()
        assert not page.is_modal_visible()
    
    @allure.story("Ингредиенты")
    @allure.title("Счетчик ингредиента увеличивается при добавлении")
    def test_ingredient_counter_increases(self, driver, base_url):
        """Проверка увеличения счетчика ингредиента"""
        driver.get(base_url)
        page = ConstructorPage(driver)
        
        initial_counter = page.get_ingredient_counter_value()
        initial_value = int(initial_counter) if initial_counter.isdigit() else 0
        logger.info(f"Начальное значение счетчика: {initial_value}")
        
        page.add_ingredient_by_drag_drop()
        
        def counter_updated(driver):
            current = int(page.get_ingredient_counter_value() or "0")
            logger.info(f"Текущее значение счетчика: {current}, начальное: {initial_value}")
            return current > initial_value
        
        page._wait.until(counter_updated)
        
        new_counter = page.get_ingredient_counter_value()
        new_value = int(new_counter) if new_counter.isdigit() else 0
        
        assert new_value > initial_value
        logger.info(f"Новое значение счетчика: {new_value}")