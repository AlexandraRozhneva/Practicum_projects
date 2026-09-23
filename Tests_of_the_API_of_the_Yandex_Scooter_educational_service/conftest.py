import pytest
from helpers.data_generators import generate_random_login, generate_random_password, generate_random_first_name
from constants.test_data import OrderTestData


@pytest.fixture
def order_data():
    """Базовые данные для заказа"""
    return {
        "first_name": generate_random_first_name(),
        "last_name": generate_random_first_name(),
        "address": OrderTestData.DEFAULT_ADDRESS,
        "metro_station": OrderTestData.DEFAULT_METRO_STATION,
        "phone": OrderTestData.DEFAULT_PHONE,
        "rent_time": OrderTestData.DEFAULT_RENT_TIME,
        "delivery_date": OrderTestData.DEFAULT_DELIVERY_DATE,
        "comment": OrderTestData.DEFAULT_COMMENT
    }


@pytest.fixture
def order_colors():
    """Данные для параметризации цветов"""
    return [
        OrderTestData.COLORS['BLACK'],
        OrderTestData.COLORS['GREY'],
        OrderTestData.COLORS['BOTH'],
        OrderTestData.COLORS['NONE']
    ]