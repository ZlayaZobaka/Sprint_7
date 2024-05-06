import requests
from data import Url

class CourierLogin():
    def __init__(self):
        self.URL = Url.BASE_URL + Url.COURIER_LOGIN_ENDPOINT

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    def login_courier(self, payload):
        response = requests.post(
            url=self.URL,
            data=payload)

        return response
