import allure
import requests
from data import Url

class CourierLogin():
    def __init__(self):
        self.URL = Url.BASE_URL + Url.COURIER_LOGIN_ENDPOINT

    @allure.step(f'Отправляем запрос на авторизацию курьера')
    def login_courier(self, payload):
        response = requests.post(
            url=self.URL,
            data=payload)

        return response
