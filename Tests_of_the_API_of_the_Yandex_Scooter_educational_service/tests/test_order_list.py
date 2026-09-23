import pytest
import allure
from api.order_api import OrderAPI


@allure.feature('Получение списка заказов')
class TestOrderList:
    
    @allure.title('Получение списка заказов возвращает список')
    def test_get_orders_returns_list(self):
        response = OrderAPI.get_orders()
        
        assert response.status_code == 200
        assert isinstance(response.json(), dict)
        assert 'orders' in response.json()
        assert isinstance(response.json()['orders'], list)
    
    @allure.title('В списке заказов есть необходимые поля')
    def test_orders_contain_required_fields(self):
        response = OrderAPI.get_orders()
        
        assert response.status_code == 200
        orders = response.json().get('orders', [])
        assert isinstance(orders, list)
        
        # Проверяем, что каждый заказ содержит поле id
        for order in orders:
            assert 'id' in order