import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import logging

logger = logging.getLogger(__name__)

class OrderPage(BasePage):
    """Страница заказа самоката"""
    
    @allure.step("Заполнение данных клиента")
    def fill_customer_data(self, name, last_name, address, metro_station, phone):
        """Заполнение данных клиента (шаг 1)"""
        logger.info(f"Заполнение данных клиента: {name} {last_name}")
        
        # Ожидаем загрузки формы
        self.wait_for_element_visible(OrderPageLocators.NAME_INPUT)
        
        # Имя
        name_input = self.wait_for_element_visible(OrderPageLocators.NAME_INPUT)
        name_input.clear()
        name_input.send_keys(name)
        
        # Фамилия
        last_name_input = self.wait_for_element_visible(OrderPageLocators.LAST_NAME_INPUT)
        last_name_input.clear()
        last_name_input.send_keys(last_name)
        
        # Адрес
        address_input = self.wait_for_element_visible(OrderPageLocators.ADDRESS_INPUT)
        address_input.clear()
        address_input.send_keys(address)
        
        # Станция метро
        metro_input = self.wait_for_element_visible(OrderPageLocators.METRO_INPUT)
        metro_input.click()
        metro_input.clear()
        metro_input.send_keys(metro_station)
        
        # Ждем появления списка станций
        try:
            self.wait_for_element_visible(OrderPageLocators.METRO_LIST)
            metro_items = self.find_elements(OrderPageLocators.METRO_ITEM)
            if metro_items:
                metro_items[0].click()
                logger.info("Выбрана станция метро из списка")
            else:
                metro_input.send_keys(Keys.ENTER)
                logger.info("Выбрана станция метро через Enter")
        except TimeoutException:
            metro_input.send_keys(Keys.ENTER)
            logger.info("Выбрана станция метро через Enter")
        
        # Телефон
        phone_input = self.wait_for_element_visible(OrderPageLocators.PHONE_INPUT)
        phone_input.clear()
        phone_input.send_keys(phone)
        
        logger.info("Данные клиента заполнены")
    
    @allure.step("Нажатие кнопки Далее")
    def click_next_button(self):
        """Нажатие кнопки Далее"""
        logger.info("Нажатие кнопки 'Далее'")
        
        # Прокручиваем к кнопке
        self.scroll_to_element(OrderPageLocators.NEXT_BUTTON)
        
        # Ждем кликабельности
        self.wait_for_element_visible(OrderPageLocators.NEXT_BUTTON)
        
        # Кликаем через JavaScript
        next_button = self.wait_for_element_visible(OrderPageLocators.NEXT_BUTTON)
        self.driver.execute_script("arguments[0].click();", next_button)
        
        logger.info("Кнопка 'Далее' нажата")
        
        # Ожидаем загрузки второй формы
        self.wait_for_second_form()
    
    @allure.step("Ожидание загрузки второй формы")
    def wait_for_second_form(self):
        """Ожидание загрузки второй формы"""
        logger.info("Ожидание загрузки второй формы...")
        
        # Ждем полной загрузки страницы
        self.wait_for_js_ready()
        
        # Проверяем, что мы перешли на второй шаг
        # Ищем заголовок "Про аренду" или поле даты
        for attempt in range(10):
            try:
                # Пробуем найти поле даты
                date_input = self.wait_for_element_visible(OrderPageLocators.DATE_INPUT)
                if date_input:
                    logger.info(f"Вторая форма загружена (попытка {attempt + 1})")
                    return
            except TimeoutException:
                logger.warning(f"Вторая форма не загрузилась, попытка {attempt + 1}")
                self.wait_for_js_ready()
        
        # Если не нашли поле даты, пробуем найти заголовок
        try:
            self.wait_for_element_visible(OrderPageLocators.DELIVERY_TITLE)
            logger.info("Вторая форма загружена (найден заголовок)")
            return
        except TimeoutException:
            pass
        
        raise TimeoutException("Вторая форма не загрузилась после 10 попыток")
    
    @allure.step("Заполнение данных доставки")
    def fill_delivery_data(self, date, rental_days, color, comment=""):
        """Заполнение данных о доставке (шаг 2)"""
        logger.info(f"Заполнение данных доставки: дата {date}, срок {rental_days} дней")
        
        # Дата доставки
        date_input = self.wait_for_element_visible(OrderPageLocators.DATE_INPUT)
        date_input.click()
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)
        logger.info(f"Введена дата: {date}")
        
        # Срок аренды
        rental_period = self.wait_for_element_visible(OrderPageLocators.RENTAL_PERIOD)
        rental_period.click()
        
        # Ждем появления опций
        self.wait_for_element_visible(OrderPageLocators.RENTAL_OPTIONS)
        rental_options = self.find_elements(OrderPageLocators.RENTAL_OPTIONS)
        
        if rental_options:
            # Выбираем нужный срок (1-7 дней)
            index = min(rental_days - 1, len(rental_options) - 1)
            rental_options[index].click()
            logger.info(f"Выбран срок аренды: {rental_days} дней")
        else:
            logger.error("Опции срока аренды не найдены")
            raise Exception("Опции срока аренды не найдены")
        
        # Выбор цвета
        if color.lower() == "black":
            self.click_element(OrderPageLocators.COLOR_BLACK)
            logger.info("Выбран черный цвет")
        elif color.lower() == "grey":
            self.click_element(OrderPageLocators.COLOR_GREY)
            logger.info("Выбран серый цвет")
        
        # Комментарий
        if comment:
            comment_input = self.wait_for_element_visible(OrderPageLocators.COMMENT_INPUT)
            comment_input.click()
            comment_input.send_keys(comment)
            logger.info(f"Добавлен комментарий: {comment}")
        
        logger.info("Данные доставки заполнены")
    
    @allure.step("Нажатие кнопки Заказать")
    def click_order_button(self):
        """Нажатие кнопки Заказать"""
        logger.info("Нажатие кнопки 'Заказать'")
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON)
        self.wait_for_element_visible(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        logger.info("Кнопка 'Заказать' нажата")
    
    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        """Подтверждение заказа"""
        logger.info("Подтверждение заказа")
        self.wait_for_element_visible(OrderPageLocators.CONFIRM_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)
        logger.info("Заказ подтвержден")
    
    @allure.step("Получение сообщения об успешном создании заказа")
    def get_order_success_message(self):
        """Получение сообщения об успешном создании заказа"""
        logger.info("Проверка сообщения об успехе")
        
        # Ждем появления модального окна
        self.wait_for_element_visible(OrderPageLocators.SUCCESS_MODAL)
        
        # Получаем текст сообщения
        success_element = self.wait_for_element_visible(OrderPageLocators.SUCCESS_MESSAGE)
        message = success_element.text
        logger.info(f"Сообщение об успехе: {message}")
        return message
    
    @allure.step("Полное оформление заказа")
    def complete_order(self, order_data):
        """Полный цикл оформления заказа"""
        # Шаг 1 - данные клиента
        self.fill_customer_data(
            order_data["name"],
            order_data["last_name"],
            order_data["address"],
            order_data["metro"],
            order_data["phone"]
        )
        
        self.click_next_button()
        
        # Шаг 2 - данные доставки
        self.fill_delivery_data(
            order_data["date"],
            order_data["rental_days"],
            order_data["color"],
            order_data.get("comment", "")
        )
        
        self.click_order_button()
        self.confirm_order()
        
        return self.get_order_success_message()