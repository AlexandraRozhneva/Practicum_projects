import pytest
import allure
import requests
from api.courier_api import CourierAPI
from constants.urls import Urls
from constants.messages import ErrorMessages
from helpers.data_generators import generate_random_login, generate_random_password
from helpers.courier_helpers import register_new_courier_and_return_login_password


@allure.feature('Логин курьера')
class TestCourierLogin:
    
    @allure.title('Курьер может авторизоваться')
    def test_courier_login_success(self):
        courier_data = register_new_courier_and_return_login_password()
        login, password, first_name = courier_data
        
        response = CourierAPI.login_courier(login, password)
        
        assert response.status_code == 200
        assert 'id' in response.json()
    
    @allure.title('Для авторизации нужны все обязательные поля')
    @pytest.mark.parametrize('empty_field, payload', [
        ('login', {"login": "", "password": generate_random_password()}),
        ('password', {"login": generate_random_login(), "password": ""})
    ])
    def test_login_empty_fields(self, empty_field, payload):
        response = requests.post(Urls.get_courier_login_url(), data=payload)
        
        assert response.status_code == 400
        assert ErrorMessages.NOT_ENOUGH_DATA in response.text
    
    @allure.title('Неправильный логин возвращает ошибку')
    def test_login_wrong_login(self):
        login = generate_random_login()
        password = generate_random_password()
        
        response = CourierAPI.login_courier(login, password)
        
        assert response.status_code == 404
        assert ErrorMessages.ACCOUNT_NOT_FOUND in response.text
    
    @allure.title('Неправильный пароль возвращает ошибку')
    def test_login_wrong_password(self):
        courier_data = register_new_courier_and_return_login_password()
        login, password, first_name = courier_data
        
        response = CourierAPI.login_courier(login, password + "wrong")
        
        assert response.status_code == 404
        assert ErrorMessages.ACCOUNT_NOT_FOUND in response.text
    
    @allure.title('Авторизация несуществующего пользователя возвращает ошибку')
    def test_login_nonexistent_user(self):
        login = generate_random_login()
        password = generate_random_password()
        
        response = CourierAPI.login_courier(login, password)
        
        assert response.status_code == 404
        assert ErrorMessages.ACCOUNT_NOT_FOUND in response.text