from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import create_driver, wait_and_find, wait_and_click, is_element_present, register_and_login_user
from locators import MainPageLocators, AuthPageLocators, AccountPageLocators

def test_go_to_personal_account():
    """Тест перехода в личный кабинет"""
    driver = None
    try:
        print("\n[Тест 1] Переход в личный кабинет")
        driver = create_driver()
        
        # Регистрация и вход пользователя
        user = register_and_login_user(driver)
        print(f"  Пользователь {user['email']} вошел в систему")
        
        # Клик по кнопке "Личный кабинет"
        wait_and_click(driver, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        
        # Проверка перехода в личный кабинет
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AccountPageLocators.PROFILE_LINK)
        )
        assert "account" in driver.current_url, "Не удалось перейти в личный кабинет"
        print("  ✅ Переход в личный кабинет работает корректно")
        
    except Exception as e:
        print(f"  ❌ Ошибка: {e}")
        raise
    finally:
        if driver:
            driver.quit()

def test_go_from_account_to_constructor():
    """Тест перехода из личного кабинета в конструктор по кнопке 'Конструктор'"""
    driver = None
    try:
        print("\n[Тест 2] Переход из личного кабинета в конструктор")
        driver = create_driver()
        
        # Регистрация и вход пользователя
        user = register_and_login_user(driver)
        print(f"  Пользователь {user['email']} вошел в систему")
        
        # Переход в личный кабинет
        wait_and_click(driver, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AccountPageLocators.PROFILE_LINK)
        )
        
        # Клик по кнопке "Конструктор"
        wait_and_click(driver, MainPageLocators.CONSTRUCTOR_BUTTON)
        
        # Проверка перехода на главную страницу
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert "account" not in driver.current_url, "Переход на главную не выполнен"
        print("  ✅ Переход из кабинета в конструктор работает корректно")
        
    except Exception as e:
        print(f"  ❌ Ошибка: {e}")
        raise
    finally:
        if driver:
            driver.quit()

def test_go_from_account_to_main_via_logo():
    """Тест перехода из личного кабинета на главную по клику на логотип"""
    driver = None
    try:
        print("\n[Тест 3] Переход на главную по клику на логотип")
        driver = create_driver()
        
        # Регистрация и вход пользователя
        user = register_and_login_user(driver)
        print(f"  Пользователь {user['email']} вошел в систему")
        
        # Переход в личный кабинет
        wait_and_click(driver, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AccountPageLocators.PROFILE_LINK)
        )
        
        # Клик по логотипу
        wait_and_click(driver, MainPageLocators.LOGO)
        
        # Проверка перехода на главную страницу
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert "account" not in driver.current_url, "Переход на главную не выполнен"
        print("  ✅ Переход по логотипу работает корректно")
        
    except Exception as e:
        print(f"  ❌ Ошибка: {e}")
        raise
    finally:
        if driver:
            driver.quit()

def test_logout_from_account():
    """Тест выхода из аккаунта"""
    driver = None
    try:
        print("\n[Тест 4] Выход из аккаунта")
        driver = create_driver()
        
        # Регистрация и вход пользователя
        user = register_and_login_user(driver)
        print(f"  Пользователь {user['email']} вошел в систему")
        
        # Переход в личный кабинет
        wait_and_click(driver, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        
        # Ждем загрузки личного кабинета и кликаем кнопку выхода
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AccountPageLocators.EXIT_BUTTON)
        ).click()
        
        # Проверка перехода на страницу входа
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AuthPageLocators.LOGIN_BUTTON)
        )
        assert "login" in driver.current_url, "Выход из аккаунта не выполнен"
        print("  ✅ Выход из аккаунта работает корректно")
        
    except Exception as e:
        print(f"  ❌ Ошибка: {e}")
        raise
    finally:
        if driver:
            driver.quit()

# Запуск тестов
if __name__ == "__main__":
    print("\n" + "="*60)
    print("ЗАПУСК ТЕСТОВ ЛИЧНОГО КАБИНЕТА")
    print("="*60)
    test_go_to_personal_account()
    test_go_from_account_to_constructor()
    test_go_from_account_to_main_via_logo()
    test_logout_from_account()