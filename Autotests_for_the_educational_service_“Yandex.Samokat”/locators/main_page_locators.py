from selenium.webdriver.common.by import By

class MainPageLocators:
    """Локаторы для главной страницы"""
    
    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    
    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    
    # Куки-баннер
    COOKIE_BANNER = (By.XPATH, "//div[@id='rcc-confirm-button']")
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")
    
    # Раздел FAQ
    FAQ_QUESTION_1 = (By.ID, "accordion__heading-0")
    FAQ_QUESTION_2 = (By.ID, "accordion__heading-1")
    FAQ_QUESTION_3 = (By.ID, "accordion__heading-2")
    FAQ_QUESTION_4 = (By.ID, "accordion__heading-3")
    FAQ_QUESTION_5 = (By.ID, "accordion__heading-4")
    FAQ_QUESTION_6 = (By.ID, "accordion__heading-5")
    FAQ_QUESTION_7 = (By.ID, "accordion__heading-6")
    FAQ_QUESTION_8 = (By.ID, "accordion__heading-7")
    
    FAQ_ANSWER_1 = (By.XPATH, "//div[@id='accordion__panel-0']/p")
    FAQ_ANSWER_2 = (By.XPATH, "//div[@id='accordion__panel-1']/p")
    FAQ_ANSWER_3 = (By.XPATH, "//div[@id='accordion__panel-2']/p")
    FAQ_ANSWER_4 = (By.XPATH, "//div[@id='accordion__panel-3']/p")
    FAQ_ANSWER_5 = (By.XPATH, "//div[@id='accordion__panel-4']/p")
    FAQ_ANSWER_6 = (By.XPATH, "//div[@id='accordion__panel-5']/p")
    FAQ_ANSWER_7 = (By.XPATH, "//div[@id='accordion__panel-6']/p")
    FAQ_ANSWER_8 = (By.XPATH, "//div[@id='accordion__panel-7']/p")
    
    # Словари для легкого доступа к вопросам и ответам
    QUESTIONS = {
        0: FAQ_QUESTION_1,
        1: FAQ_QUESTION_2,
        2: FAQ_QUESTION_3,
        3: FAQ_QUESTION_4,
        4: FAQ_QUESTION_5,
        5: FAQ_QUESTION_6,
        6: FAQ_QUESTION_7,
        7: FAQ_QUESTION_8,
    }
    
    ANSWERS = {
        0: FAQ_ANSWER_1,
        1: FAQ_ANSWER_2,
        2: FAQ_ANSWER_3,
        3: FAQ_ANSWER_4,
        4: FAQ_ANSWER_5,
        5: FAQ_ANSWER_6,
        6: FAQ_ANSWER_7,
        7: FAQ_ANSWER_8,
    }