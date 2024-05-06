import requests
from data import Url


class Courier:
    def __init__(self):
        self.URL = Url.BASE_URL + Url.COURIER_ENDPOINT

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    def create_new_courier(self, payload):
        response = requests.post(
            url=self.URL,
            data=payload)

        return response

    def delete_courier(self, courier_id):
        response = requests.delete(url=self.URL + f'/{courier_id}')

        return response
