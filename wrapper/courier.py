import allure
import requests
from data import Url


class Courier:
    def __init__(self):
        self.URL = Url.BASE_URL + Url.COURIER_ENDPOINT

    @allure.step(f'Отправляем запрос на создание нового курьера')
    def create_new_courier(self, payload):
        response = requests.post(
            url=self.URL,
            data=payload)

        return response

    @allure.step(f'Отправляем запрос на удаление курьера')
    def delete_courier(self, courier_id):
        response = requests.delete(url=self.URL + f'/{courier_id}')

        return response
