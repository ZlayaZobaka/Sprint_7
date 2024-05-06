import requests
from data import Url
import json


class Orders:
    def __init__(self):
        self.URL = Url.BASE_URL + Url.ORDER_ENDPOINT

    # отправляем запрос на создание заказа и сохраняем ответ в переменную response
    def create_new_order(self, payload):
        response = requests.post(
            url=self.URL,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"})

        return response

    # отправляем запрос на получение списка заказов и сохраняем ответ в переменную response
    def get_orders(self, courier_id="", nearest_station="", limit="", page=""):
        url = self.URL
        if courier_id or nearest_station or limit or page:
            url.join('?')
            if courier_id:
                url.join(f'courierId = {courier_id}')
            if nearest_station:
                url.join(f'nearestStation={nearest_station}')
            if limit:
                url.join(f'limit={limit}')
            if page:
                url.join(f'page={page}')
        response = requests.get(
            url=url)

        return response
