import allure
import requests
from constants.urls import Urls


class CourierAPI:
    
    @staticmethod
    @allure.step("Создание курьера с логином: {login}")
    def create_courier(login, password, first_name=None):
        """Создание курьера"""
        payload = {
            "login": login,
            "password": password
        }
        if first_name:
            payload["firstName"] = first_name
            
        return requests.post(Urls.get_courier_url(), data=payload)
    
    @staticmethod
    @allure.step("Авторизация курьера с логином: {login}")
    def login_courier(login, password):
        """Авторизация курьера"""
        payload = {
            "login": login,
            "password": password
        }
        return requests.post(Urls.get_courier_login_url(), data=payload)
    
    @staticmethod
    @allure.step("Удаление курьера с ID: {courier_id}")
    def delete_courier(courier_id):
        """Удаление курьера"""
        return requests.delete(Urls.get_courier_delete_url(courier_id))