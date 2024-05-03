from wrapper.base import Base
import requests
import data

class CourierLogin(Base):
    def __init__(self):
        self.URL = f'{data.BASE_URL}/courier/login'

    def login_courier_payload(self, payload, login=True, password=True):
        del payload['firstName']

        if not login:
            del payload['login']

        if not password:
            del payload['password']

        return payload

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    def login_courier(self, payload):
        response = requests.post(
            url=self.URL,
            data=payload)

        return response
