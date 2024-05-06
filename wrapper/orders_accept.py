import requests
from data import Url


class OrdersAccept:
    def __init__(self):
        self.URL = Url.BASE_URL + Url.ORDER_ACCEPT_ENDPOINT

    # Получить заказ по его номеру
    def accept_orders(self, order_id, courier_id):
        response = requests.put(
            url=f'{self.URL}/{order_id}?courierId={courier_id}')

        return response
