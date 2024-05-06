import requests
from data import Url


class OrdersTrack:
    def __init__(self):
        self.URL = Url.BASE_URL + Url.ORDER_TRACK_ENDPOINT

    # Получить заказ по его номеру
    def track_order(self, t):
        response = requests.get(
            url=f'{self.URL}?t={t}')

        return response
