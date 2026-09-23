class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'
    COURIER = '/courier'
    COURIER_LOGIN = '/courier/login'
    ORDERS = '/orders'
    ORDERS_CANCEL = '/orders/cancel'
    
    @classmethod
    def get_courier_url(cls):
        return f'{cls.BASE_URL}{cls.COURIER}'
    
    @classmethod
    def get_courier_login_url(cls):
        return f'{cls.BASE_URL}{cls.COURIER_LOGIN}'
    
    @classmethod
    def get_orders_url(cls):
        return f'{cls.BASE_URL}{cls.ORDERS}'
    
    @classmethod
    def get_courier_delete_url(cls, courier_id):
        return f'{cls.BASE_URL}{cls.COURIER}/{courier_id}'