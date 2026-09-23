import requests
import allure
from helpers.data_generators import BASE_URL

@allure.step("Регистрация пользователя")
def register_user(user_data):
    """Отправка POST-запроса на регистрацию пользователя."""
    return requests.post(f"{BASE_URL}/auth/register", json=user_data)

@allure.step("Авторизация пользователя")
def login_user(login_data):
    """Отправка POST-запроса на авторизацию пользователя."""
    return requests.post(f"{BASE_URL}/auth/login", json=login_data)

@allure.step("Создание заказа")
def create_order(order_data, token=None):
    """Отправка POST-запроса на создание заказа."""
    headers = {"Authorization": token} if token else {}
    return requests.post(f"{BASE_URL}/orders", json=order_data, headers=headers)

@allure.step("Удаление пользователя")
def delete_user(token):
    """Отправка DELETE-запроса на удаление пользователя."""
    headers = {"Authorization": token}
    return requests.delete(f"{BASE_URL}/auth/user", headers=headers)

@allure.step("Получение списка ингредиентов")
def get_ingredients():
    """Отправка GET-запроса на получение ингредиентов."""
    return requests.get(f"{BASE_URL}/ingredients")