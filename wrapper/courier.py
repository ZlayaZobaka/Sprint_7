from wrapper.base import Base
import requests
import data
class Courier(Base):
    def __init__(self):
        self.URL = f'{data.BASE_URL}/courier'

    def create_new_courier_payload1(self, login=True, password=True):
        payload = {
            "firstName": self.generate_random_string(10)
        }
        if login:
            payload['login'] = self.generate_random_string(10)

        if password:
            payload['password'] = self.generate_random_string(10)

        return payload

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    def create_new_courier(self, payload):
        response = requests.post(
            url=self.URL,
            data=payload)

        return response
