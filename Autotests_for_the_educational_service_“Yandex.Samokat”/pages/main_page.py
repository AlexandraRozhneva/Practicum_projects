import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import logging

logger = logging.getLogger(__name__)

class MainPage(BasePage):
    """Главная страница сервиса Самокат"""
    
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.url = "https://qa-scooter.praktikum-services.ru/"
    
    @allure.step("Открытие главной страницы")
    def open(self):
        """Открытие главной страницы"""
        self.driver.get(self.url)
        self.wait_for_js_ready()
        logger.info(f"Открыта страница: {self.url}")
    
    @allure.step("Закрытие куки-баннера")
    def close_cookie_banner(self):
        """Закрытие куки-баннера"""
        try:
            self.wait_for_element_visible(MainPageLocators.COOKIE_ACCEPT_BUTTON)
            self.click_element(MainPageLocators.COOKIE_ACCEPT_BUTTON)
            logger.info("Куки-баннер закрыт")
        except:
            logger.info("Куки-баннер не найден или уже закрыт")
    
    @allure.step("Клик по кнопке заказа вверху страницы")
    def click_order_button_top(self):
        """Клик по кнопке заказа вверху страницы"""
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_TOP)
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)
        logger.info("Нажата кнопка заказа (вверху)")
    
    @allure.step("Клик по кнопке заказа внизу страницы")
    def click_order_button_bottom(self):
        """Клик по кнопке заказа внизу страницы"""
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        logger.info("Нажата кнопка заказа (внизу)")
    
    @allure.step("Клик по вопросу в разделе FAQ: {question_index}")
    def click_faq_question(self, question_index):
        """Клик по вопросу в разделе FAQ"""
        question_locator = MainPageLocators.QUESTIONS[question_index]
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)
        logger.info(f"Нажат вопрос {question_index + 1}")
    
    @allure.step("Получение текста ответа на вопрос: {question_index}")
    def get_faq_answer_text(self, question_index):
        """Получение текста ответа на вопрос"""
        answer_locator = MainPageLocators.ANSWERS[question_index]
        self.wait_for_element_visible(answer_locator)
        return self.get_text(answer_locator)
    
    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        """Клик по логотипу Самоката"""
        self.click_element(MainPageLocators.SCOOTER_LOGO)
        logger.info("Клик по логотипу Самоката")
    
    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        """Клик по логотипу Яндекса"""
        self.scroll_to_element(MainPageLocators.YANDEX_LOGO)
        self.click_element(MainPageLocators.YANDEX_LOGO)
        logger.info("Клик по логотипу Яндекса")