from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import create_driver, wait_and_find, wait_and_click, is_element_present, register_user, login_user
from locators import MainPageLocators, AuthPageLocators

def test_login_via_main_button():
    """Тест входа по кнопке 'Войти в аккаунт' на главной"""
    driver = None
    try:
        print("\n[Тест 1] Вход через кнопку 'Войти в аккаунт' на главной")
        driver = create_driver()
        
        # Регистрация пользователя
        user = register_user(driver)
        print(f"  Зарегистрирован пользователь: {user['email']}")
        
        driver.get("https://stellarburgers.education-services.ru/")
        
        # Клик по кнопке "Войти в аккаунт"
        wait_and_click(driver, MainPageLocators.LOGIN_BUTTON_MAIN)
        
        # Вход в систему
        login_user(driver, user["email"], user["password"])
        
        # Проверка успешного входа
        assert is_element_present(driver, MainPageLocators.ORDER_BUTTON), "Кнопка оформления заказа не найдена"
        print("  ✅ Вход через главную кнопку работает корректно")
        
    except Exception as e:
        print(f"  ❌ Ошибка: {e}")
        raise
    finally:
        if driver:
            driver.quit()

def test_login_via_personal_account_button():
    """Тест входа через кнопку 'Личный кабинет'"""
    driver = None
    try:
        print("\n[Тест 2] Вход через кнопку 'Личный кабинет'")
        driver = create_driver()
        
        # Регистрация пользователя
        user = register_user(driver)
        print(f"  Зарегистрирован пользователь: {user['email']}")
        
        driver.get("https://stellarburgers.education-services.ru/")
        
        # Клик по кнопке "Личный кабинет"
        wait_and_click(driver, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        
        # Вход в систему
        login_user(driver, user["email"], user["password"])
        
        # Проверка успешного входа
        assert is_element_present(driver, MainPageLocators.ORDER_BUTTON), "Кнопка оформления заказа не найдена"
        print("  ✅ Вход через личный кабинет работает корректно")
        
    except Exception as e:
        print(f"  ❌ Ошибка: {e}")
        raise
    finally:
        if driver:
            driver.quit()

def test_login_via_register_form():
    """Тест входа через кнопку в форме регистрации"""
    driver = None
    try:
        print("\n[Тест 3] Вход через кнопку в форме регистрации")
        driver = create_driver()
        
        # Регистрация пользователя
        user = register_user(driver)
        print(f"  Зарегистрирован пользователь: {user['email']}")
        
        driver.get("https://stellarburgers.education-services.ru/register")
        
        # Клик по ссылке "Войти"
        wait_and_click(driver, AuthPageLocators.LOGIN_LINK)
        
        # Вход в систему
        login_user(driver, user["email"], user["password"])
        
        # Проверка успешного входа
        assert is_element_present(driver, MainPageLocators.ORDER_BUTTON), "Кнопка оформления заказа не найдена"
        print("  ✅ Вход через форму регистрации работает корректно")
        
    except Exception as e:
        print(f"  ❌ Ошибка: {e}")
        raise
    finally:
        if driver:
            driver.quit()

def test_login_via_password_recovery_form():
    """Тест входа через кнопку в форме восстановления пароля"""
    driver = None
    try:
        print("\n[Тест 4] Вход через кнопку в форме восстановления пароля")
        driver = create_driver()
        
        # Регистрация пользователя
        user = register_user(driver)
        print(f"  Зарегистрирован пользователь: {user['email']}")
        
        driver.get("https://stellarburgers.education-services.ru/forgot-password")
        
        # Клик по ссылке "Войти"
        wait_and_click(driver, AuthPageLocators.LOGIN_LINK)
        
        # Вход в систему
        login_user(driver, user["email"], user["password"])
        
        # Проверка успешного входа
        assert is_element_present(driver, MainPageLocators.ORDER_BUTTON), "Кнопка оформления заказа не найдена"
        print("  ✅ Вход через форму восстановления пароля работает корректно")
        
    except Exception as e:
        print(f"  ❌ Ошибка: {e}")
        raise
    finally:
        if driver:
            driver.quit()

# Запуск тестов
if __name__ == "__main__":
    print("\n" + "="*60)
    print("ЗАПУСК ТЕСТОВ ВХОДА")
    print("="*60)
    test_login_via_main_button()
    test_login_via_personal_account_button()
    test_login_via_register_form()
    test_login_via_password_recovery_form()