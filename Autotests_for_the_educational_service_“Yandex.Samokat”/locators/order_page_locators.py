from selenium.webdriver.common.by import By

class OrderPageLocators:
    """Локаторы для страницы заказа"""
    
    # Шаг 1: Данные клиента
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Выбор станции метро
    METRO_ITEM = (By.XPATH, "//div[@class='select-search__select']//button")
    METRO_LIST = (By.XPATH, "//div[@class='select-search__select']")
    
    # Шаг 2: Данные о доставке
    ORDER_FORM_TITLE = (By.XPATH, "//div[contains(@class, 'Order_Header') and text()='Для кого самокат']")
    DELIVERY_TITLE = (By.XPATH, "//div[contains(@class, 'Order_Header') and text()='Про аренду']")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    RENTAL_OPTIONS = (By.XPATH, "//div[contains(@class, 'Dropdown-option')]")
    
    # Цвет самоката
    COLOR_BLACK = (By.XPATH, "//input[@id='black']")
    COLOR_GREY = (By.XPATH, "//input[@id='grey']")
    
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    CANCEL_BUTTON = (By.XPATH, "//button[text()='Нет']")
    
    # Успешное создание заказа
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
    SUCCESS_TEXT = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]//div[text()='Заказ оформлен']")