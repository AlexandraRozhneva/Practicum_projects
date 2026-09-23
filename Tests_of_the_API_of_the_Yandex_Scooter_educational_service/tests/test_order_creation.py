import pytest
import allure
from api.order_api import OrderAPI


@allure.feature('Создание заказа')
class TestOrderCreation:
    
    @allure.title('Создание заказа с разными цветами')
    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY'],
        None
    ])
    def test_create_order_with_colors(self, order_data, color):
        response = OrderAPI.create_order(**order_data, color=color)
        
        assert response.status_code == 201
        track = response.json().get('track')
        assert track is not None
        assert isinstance(track, int)