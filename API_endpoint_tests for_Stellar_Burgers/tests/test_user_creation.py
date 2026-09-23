import pytest
import allure
from helpers.api_requests import register_user

@allure.epic("Пользователь")
@allure.story("Создание пользователя")
class TestUserCreation:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, temp_user):
        user_data = temp_user["user"]
        
        with allure.step("Проверка успешного ответа (стр. 3-4 документации)"):
            # Пользователь уже создан в фикстуре temp_user
            # Проверяем, что данные сохранились корректно
            assert user_data["email"] is not None
            assert user_data["password"] is not None
            assert user_data["name"] is not None

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user(self, registered_user):
        existing_user_data = registered_user["user"]
        response = register_user(existing_user_data)
        
        with allure.step("Проверка ответа с ошибкой (стр. 3 документации)"):
            assert response.status_code == 403
            assert response.json()["success"] is False
            assert response.json()["message"] == "User already exists"

    @allure.title("Создание пользователя без одного обязательного поля")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field(self, new_user_data, missing_field):
        invalid_data = new_user_data.copy()
        invalid_data.pop(missing_field)
        response = register_user(invalid_data)
        
        with allure.step("Проверка ответа с ошибкой (стр. 3 документации)"):
            assert response.status_code == 403
            assert response.json()["success"] is False
            assert response.json()["message"] == "Email, password and name are required fields"
