import allure
import requests
from constants.urls import Urls


class OrderAPI:
    
    @staticmethod
    @allure.step("Создание заказа для {first_name} {last_name}")
    def create_order(first_name, last_name, address, metro_station, phone,
                     rent_time, delivery_date, comment, color=None):
        """Создание заказа"""
        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment
        }
        if color:
            payload["color"] = color
            
        return requests.post(Urls.get_orders_url(), json=payload)
    
    @staticmethod
    @allure.step("Получение списка заказов")
    def get_orders():
        """Получение списка заказов"""
        return requests.get(Urls.get_orders_url())
    
    @staticmethod
    @allure.step("Отмена заказа по треку: {track}")
    def cancel_order(track):
        """Отмена заказа по треку"""
        return requests.put(
            Urls.get_orders_url() + '/cancel',
            params={'track': track}
        )