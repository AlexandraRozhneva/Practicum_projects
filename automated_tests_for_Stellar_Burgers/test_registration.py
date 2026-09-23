from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import create_driver, wait_and_find, wait_and_click, is_element_present
from locators import AuthPageLocators
from generators import generate_email, generate_password, generate_name, generate_invalid_password

def test_successful_registration():
    """Тест успешной регистрации"""
    driver = None
    try:
        print("\n[Тест 1] Успешная регистрация")
        driver = create_driver()
        
        email = generate_email()
        password = generate_password()
        name = generate_name()
        
        print(f"  Регистрация с данными: {email}, {name}")
        driver.get("https://stellarburgers.education-services.ru/register")
        
        # Заполнение формы регистрации
        wait_and_find(driver, AuthPageLocators.NAME_INPUT).send_keys(name)
        wait_and_find(driver, AuthPageLocators.EMAIL_INPUT).send_keys(email)
        wait_and_find(driver, AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        wait_and_click(driver, AuthPageLocators.REGISTER_BUTTON)
        
        # Проверка перенаправления на страницу входа
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )
        
        # Проверка наличия формы входа
        assert is_element_present(driver, AuthPageLocators.LOGIN_BUTTON), "Страница входа не загрузилась"
        print("  ✅ Успешная регистрация работает корректно")
        
    except Exception as e:
        print(f"  ❌ Ошибка: {e}")
        raise
    finally:
        if driver:
            driver.quit()

def test_registration_with_invalid_password():
    """Тест регистрации с некорректным паролем (менее 6 символов)"""
    driver = None
    try:
        print("\n[Тест 2] Регистрация с некорректным паролем")
        driver = create_driver()
        
        email = generate_email()
        invalid_password = generate_invalid_password()
        name = generate_name()
        
        print(f"  Попытка регистрации с паролем '{invalid_password}' (длина {len(invalid_password)})")
        driver.get("https://stellarburgers.education-services.ru/register")
        
        wait_and_find(driver, AuthPageLocators.NAME_INPUT).send_keys(name)
        wait_and_find(driver, AuthPageLocators.EMAIL_INPUT).send_keys(email)
        wait_and_find(driver, AuthPageLocators.PASSWORD_INPUT).send_keys(invalid_password)
        wait_and_click(driver, AuthPageLocators.REGISTER_BUTTON)
        
        # Проверка появления сообщения об ошибке
        error_message = wait_and_find(driver, AuthPageLocators.PASSWORD_ERROR)
        assert error_message.is_displayed(), "Сообщение об ошибке не появилось"
        assert "Некорректный пароль" in error_message.text, "Текст ошибки не соответствует"
        
        # Проверка, что регистрация не произошла
        assert "register" in driver.current_url, "Произошел переход со страницы регистрации"
        print("  ✅ Ошибка для некорректного пароля отображается корректно")
        
    except Exception as e:
        print(f"  ❌ Ошибка: {e}")
        raise
    finally:
        if driver:
            driver.quit()

def test_registration_with_empty_name():
    """Тест регистрации с пустым именем"""
    driver = None
    try:
        print("\n[Тест 3] Регистрация с пустым именем")
        driver = create_driver()
        
        email = generate_email()
        password = generate_password()
        
        print(f"  Попытка регистрации с пустым именем, email: {email}")
        driver.get("https://stellarburgers.education-services.ru/register")
        
        wait_and_find(driver, AuthPageLocators.NAME_INPUT).send_keys("")
        wait_and_find(driver, AuthPageLocators.EMAIL_INPUT).send_keys(email)
        wait_and_find(driver, AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        wait_and_click(driver, AuthPageLocators.REGISTER_BUTTON)
        
        # Проверка, что регистрация не произошла
        assert "register" in driver.current_url, "Произошел переход со страницы регистрации"
        print("  ✅ Регистрация с пустым именем не проходит (корректное поведение)")
        
    except Exception as e:
        print(f"  ❌ Ошибка: {e}")
        raise
    finally:
        if driver:
            driver.quit()

def test_registration_with_invalid_email():
    """Тест регистрации с некорректным email"""
    driver = None
    try:
        print("\n[Тест 4] Регистрация с некорректным email")
        driver = create_driver()
        
        invalid_email = "invalid_email_without_at_symbol"
        password = generate_password()
        name = generate_name()
        
        print(f"  Попытка регистрации с email: {invalid_email}")
        driver.get("https://stellarburgers.education-services.ru/register")
        
        wait_and_find(driver, AuthPageLocators.NAME_INPUT).send_keys(name)
        wait_and_find(driver, AuthPageLocators.EMAIL_INPUT).send_keys(invalid_email)
        wait_and_find(driver, AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        wait_and_click(driver, AuthPageLocators.REGISTER_BUTTON)
        
        # Проверка, что регистрация не произошла
        assert "register" in driver.current_url, "Произошел переход со страницы регистрации"
        print("  ✅ Регистрация с некорректным email не проходит (корректное поведение)")
        
    except Exception as e:
        print(f"  ❌ Ошибка: {e}")
        raise
    finally:
        if driver:
            driver.quit()

# Запуск тестов
if __name__ == "__main__":
    print("\n" + "="*60)
    print("ЗАПУСК ТЕСТОВ РЕГИСТРАЦИИ")
    print("="*60)
    test_successful_registration()
    test_registration_with_invalid_password()
    test_registration_with_empty_name()
    test_registration_with_invalid_email()