from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderModal(BasePage):
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_close')]")

    def get_order_number(self):
        """Получение номера заказа"""
        return self.get_text(self.ORDER_NUMBER)
    
    def close_modal(self):
        """Закрытие модального окна"""
        self.click_element(self.CLOSE_BUTTON)
        self.wait_for_element_disappear(self.ORDER_NUMBER)