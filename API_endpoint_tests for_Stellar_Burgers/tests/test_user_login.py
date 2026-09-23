import allure
from helpers.api_requests import login_user

@allure.epic("Пользователь")
@allure.story("Авторизация пользователя")
class TestUserLogin:

    @allure.title("Вход под существующим пользователем")
    def test_login_existing_user(self, registered_user):
        user_data = registered_user["user"]
        login_data = {"email": user_data["email"], "password": user_data["password"]}
        response = login_user(login_data)
        
        with allure.step("Проверка успешного ответа (стр. 3 документации)"):
            assert response.status_code == 200
            assert response.json()["success"] is True
            assert response.json()["user"]["email"] == user_data["email"]
            assert response.json()["user"]["name"] == user_data["name"]
            assert "accessToken" in response.json()
            assert "refreshToken" in response.json()

    @allure.title("Вход с неверным логином")
    def test_login_invalid_email(self):
        login_data = {"email": "wrong@test.com", "password": "any_password"}
        response = login_user(login_data)
        
        with allure.step("Проверка ответа с ошибкой (стр. 4 документации)"):
            assert response.status_code == 401
            assert response.json()["success"] is False
            assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Вход с неверным паролем")
    def test_login_invalid_password(self, registered_user):
        user_data = registered_user["user"]
        login_data = {"email": user_data["email"], "password": "wrong_password"}
        response = login_user(login_data)
        
        with allure.step("Проверка ответа с ошибкой (стр. 4 документации)"):
            assert response.status_code == 401
            assert response.json()["success"] is False
            assert response.json()["message"] == "email or password are incorrect"