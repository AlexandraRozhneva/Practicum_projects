import requests
from constants.urls import Urls
from helpers.data_generators import generate_random_login, generate_random_password, generate_random_first_name


def register_new_courier_and_return_login_password():
    """
    Регистрирует нового курьера и возвращает список [логин, пароль, имя]
    Если регистрация не удалась, возвращает пустой список
    """
    login = generate_random_login()
    password = generate_random_password()
    first_name = generate_random_first_name()
    
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    
    response = requests.post(Urls.get_courier_url(), data=payload)
    
    if response.status_code == 201:
        return [login, password, first_name]
    
    return []