from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
import logging
import re

logger = logging.getLogger(__name__)


class ConstructorPage(BasePage):
    # Локаторы навигации
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")
    
    # Локаторы для ингредиентов
    BUN_INGREDIENT = (By.XPATH, "//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa6d')]")
    
    # Локатор для корзины сборки
    CONSTRUCTOR_BASKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    
    # Локаторы для модального окна ингредиента
    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//button")
    
    # Локаторы для авторизации и регистрации
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']")
    REGISTER_SUBMIT = (By.XPATH, "//button[text()='Зарегистрироваться']")
    
    # Поля ввода для регистрации
    NAME_INPUT_REGISTER = (By.XPATH, "(//input[@type='text' and @name='name'])[1]")
    EMAIL_INPUT_REGISTER = (By.XPATH, "(//input[@type='text' and @name='name'])[2]")
    PASSWORD_INPUT_REGISTER = (By.XPATH, "//input[@type='password' and @name='Пароль']")
    
    # Поля ввода для авторизации
    EMAIL_INPUT_LOGIN = (By.XPATH, "//input[@type='text' and @name='name']")
    PASSWORD_INPUT_LOGIN = (By.XPATH, "//input[@type='password' and @name='Пароль']")
    
    # Локаторы для оформления заказа
    CHECKOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_button')]")
    ORDER_NUMBER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//h2[contains(@class, 'text_type_digits-large')]")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    ORDER_LOADER = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//div[contains(@class, 'loader')]")
    
    # Локатор для счетчика ингредиента
    INGREDIENT_COUNTER = (By.XPATH, "//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa6d')]//p[contains(@class, 'counter')]")

    @allure.step("Переход на конструктор")
    def click_constructor(self):
        """Переход на конструктор"""
        self.click_element_by_js(self.CONSTRUCTOR_BUTTON)
        logger.info("Перешли в конструктор")

    @allure.step("Переход в ленту заказов")
    def click_order_feed(self):
        """Переход в ленту заказов"""
        self.click_element_by_js(self.ORDER_FEED_BUTTON)
        logger.info("Перешли в ленту заказов")

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        """Клик по ингредиенту для открытия модального окна"""
        self.scroll_to_element(self.BUN_INGREDIENT)
        self.click_element_by_js(self.BUN_INGREDIENT)

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        """Закрытие модального окна"""
        try:
            self.click_element_by_js(self.MODAL_CLOSE_BUTTON)
        except:
            pass
        self.wait_for_element_disappear(self.INGREDIENT_MODAL)

    @allure.step("Проверка видимости модального окна")
    def is_modal_visible(self):
        """Проверка видимости модального окна"""
        return self.is_element_visible(self.INGREDIENT_MODAL)

    @allure.step("Добавление ингредиента через drag-and-drop")
    def add_ingredient_by_drag_drop(self):
        """Добавление ингредиента через drag-and-drop с поддержкой всех браузеров"""
        logger.info("Добавляем ингредиент в корзину")
        
        self.scroll_to_element(self.BUN_INGREDIENT)
        self.scroll_to_element(self.CONSTRUCTOR_BASKET)
        
        browser_name = self.get_capabilities().get('browserName', '').lower()
        logger.info(f"Браузер: {browser_name}")
        
        if browser_name == 'firefox':
            self._drag_and_drop_firefox(self.BUN_INGREDIENT, self.CONSTRUCTOR_BASKET)
        else:
            self._drag_and_drop_chrome(self.BUN_INGREDIENT, self.CONSTRUCTOR_BASKET)

    def _drag_and_drop_firefox(self, source_locator, target_locator):
        """Drag-and-drop для Firefox через JavaScript"""
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        
        source_rect = self.execute_script("""
            var rect = arguments[0].getBoundingClientRect();
            return {left: rect.left, top: rect.top, width: rect.width, height: rect.height};
        """, source)
        
        target_rect = self.execute_script("""
            var rect = arguments[0].getBoundingClientRect();
            return {left: rect.left, top: rect.top, width: rect.width, height: rect.height};
        """, target)
        
        source_x = source_rect['left'] + source_rect['width'] / 2
        source_y = source_rect['top'] + source_rect['height'] / 2
        target_x = target_rect['left'] + target_rect['width'] / 2
        target_y = target_rect['top'] + target_rect['height'] / 2
        
        js_script = """
        function fireDragEvent(element, eventType, clientX, clientY, dataTransfer) {
            const event = new DragEvent(eventType, {
                bubbles: true,
                cancelable: true,
                view: window,
                clientX: clientX,
                clientY: clientY,
                dataTransfer: dataTransfer
            });
            element.dispatchEvent(event);
            return event;
        }
        
        function simulateDragDrop(source, target, sourceX, sourceY, targetX, targetY) {
            const dataTransfer = new DataTransfer();
            fireDragEvent(source, 'dragstart', sourceX, sourceY, dataTransfer);
            fireDragEvent(target, 'dragenter', targetX, targetY, dataTransfer);
            fireDragEvent(target, 'dragover', targetX, targetY, dataTransfer);
            fireDragEvent(target, 'drop', targetX, targetY, dataTransfer);
            fireDragEvent(source, 'dragend', sourceX, sourceY, dataTransfer);
            return true;
        }
        
        const source = arguments[0];
        const target = arguments[1];
        const sourceX = arguments[2];
        const sourceY = arguments[3];
        const targetX = arguments[4];
        const targetY = arguments[5];
        
        return simulateDragDrop(source, target, sourceX, sourceY, targetX, targetY);
        """
        
        self.execute_script(js_script, source, target, source_x, source_y, target_x, target_y)
        logger.info("Drag-and-drop выполнен для Firefox")

    def _drag_and_drop_chrome(self, source_locator, target_locator):
        """Drag-and-drop для Chrome через ActionChains"""
        self.drag_and_drop(source_locator, target_locator)

    @allure.step("Получение значения счетчика ингредиента")
    def get_ingredient_counter_value(self):
        """Получение значения счетчика ингредиента"""
        try:
            counter_text = self.get_text(self.INGREDIENT_COUNTER)
            numbers = re.findall(r'\d+', counter_text)
            return numbers[0] if numbers else "0"
        except:
            return "0"

    def find_element_with_retry(self, locators):
        """Пытается найти элемент по нескольким локаторам"""
        for locator in locators:
            try:
                element = self.find_element(locator)
                logger.info(f"Элемент найден по локатору: {locator}")
                return element
            except Exception as e:
                logger.warning(f"Не удалось найти элемент по локатору {locator}: {e}")
                continue
        raise Exception(f"Элемент не найден ни по одному из локаторов: {locators}")

    @allure.step("Регистрация пользователя")
    def register_user(self, email, password, name):
        """Регистрация нового пользователя"""
        logger.info(f"Начинаем регистрацию пользователя: {email}")
        
        self.get("https://stellarburgers.education-services.ru/register")
        self.wait_for_element((By.TAG_NAME, "body"))
        
        name_input = self.find_element(self.NAME_INPUT_REGISTER)
        name_input.clear()
        name_input.send_keys(name)
        logger.info(f"Введено имя: {name}")
        
        email_input = self.find_element(self.EMAIL_INPUT_REGISTER)
        email_input.clear()
        email_input.send_keys(email)
        logger.info(f"Введен email: {email}")
        
        password_input = self.find_element(self.PASSWORD_INPUT_REGISTER)
        password_input.clear()
        password_input.send_keys(password)
        logger.info("Введен пароль")
        
        self.click_element_by_js(self.REGISTER_SUBMIT)
        logger.info("Нажата кнопка 'Зарегистрироваться'")
        
        self.wait_for_url_contains("/login")
        logger.info("Перенаправлены на страницу логина")
        
        self.wait_for_element(self.LOGIN_BUTTON)
        logger.info(f"Пользователь {email} успешно зарегистрирован")

    @allure.step("Авторизация пользователя")
    def login_user(self, email, password):
        """Авторизация пользователя"""
        logger.info(f"Начинаем авторизацию пользователя: {email}")
        
        self.get("https://stellarburgers.education-services.ru/login")
        self.wait_for_element((By.TAG_NAME, "body"))
        
        email_input = self.find_element(self.EMAIL_INPUT_LOGIN)
        email_input.clear()
        email_input.send_keys(email)
        logger.info(f"Введен email: {email}")
        
        password_input = self.find_element(self.PASSWORD_INPUT_LOGIN)
        password_input.clear()
        password_input.send_keys(password)
        logger.info("Введен пароль")
        
        self.click_element_by_js(self.LOGIN_BUTTON)
        logger.info("Нажата кнопка 'Войти'")
        
        self.wait_for_element(self.CONSTRUCTOR_BUTTON)
        logger.info(f"Пользователь {email} успешно авторизован")

    @allure.step("Создание заказа")
    def create_order(self):
        """Создание заказа"""
        logger.info("Начинаем создание заказа")
        
        self.add_ingredient_by_drag_drop()
        
        # Находим все кнопки на странице
        buttons = self.find_elements_by_xpath("//button")
        logger.info(f"Найдено кнопок на странице: {len(buttons)}")
        
        # Ищем кнопку оформления заказа
        checkout_button = None
        for button in buttons:
            button_text = button.text
            if "Оформить" in button_text:
                checkout_button = button
                logger.info(f"Найдена кнопка с текстом: '{button_text}'")
                break
        
        if checkout_button:
            self.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
            self.execute_script("arguments[0].click();", checkout_button)
            logger.info("Кликнули по кнопке 'Оформить заказ'")
        else:
            raise Exception("Не удалось найти кнопку оформления заказа")
        
        self.wait_for_element(self.ORDER_NUMBER_MODAL)
        logger.info("Модальное окно с номером заказа появилось")
        
        self._wait_for_order_number_update()

    def _wait_for_order_number_update(self, timeout=60):
        """Ожидание обновления номера заказа с 9999 на реальный номер"""
        logger.info(f"Ожидаем обновления номера заказа (таймаут: {timeout} секунд)...")
        
        def order_number_updated(driver):
            try:
                order_text = self.get_text(self.ORDER_NUMBER_MODAL)
                logger.info(f"Текущий номер заказа: '{order_text}'")
                
                numbers = re.findall(r'\d+', order_text)
                if numbers:
                    current_number = numbers[0]
                    if current_number != "9999" and len(current_number) >= 6:
                        logger.info(f"Номер заказа обновился на: {current_number}")
                        return True
                return False
            except Exception as e:
                logger.warning(f"Ошибка при проверке номера заказа: {e}")
                return False
        
        self.wait_for_condition(order_number_updated, timeout)
        logger.info("Номер заказа успешно обновился")

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        """Получение номера заказа"""
        try:
            order_text = self.get_text(self.ORDER_NUMBER_MODAL)
            logger.info(f"Получен текст с номером заказа: '{order_text}'")
            
            numbers = re.findall(r'\d+', order_text)
            if not numbers:
                logger.error(f"Не найдены цифры в тексте: {order_text}")
                return None
            
            order_number = numbers[0]
            
            if order_number == "9999":
                logger.warning("Получен тестовый номер 9999, ожидаем обновления...")
                self._wait_for_order_number_update()
                order_text = self.get_text(self.ORDER_NUMBER_MODAL)
                numbers = re.findall(r'\d+', order_text)
                order_number = numbers[0] if numbers else None
            
            logger.info(f"Извлечен номер заказа: {order_number}")
            return order_number
            
        except Exception as e:
            logger.error(f"Ошибка при получении номера заказа: {e}")
            return None

    @allure.step("Проверка видимости модального окна заказа")
    def is_order_modal_visible(self):
        """Проверка видимости модального окна заказа"""
        return self.is_element_visible(self.ORDER_NUMBER_MODAL)

    @allure.step("Закрытие модального окна заказа")
    def close_order_modal(self):
        """Закрытие модального окна заказа"""
        try:
            self.click_element_by_js(self.MODAL_CLOSE_BUTTON)
            logger.info("Модальное окно заказа закрыто")
        except:
            pass
        self.wait_for_element_disappear(self.ORDER_MODAL)