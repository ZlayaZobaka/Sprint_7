import allure
import requests
import helpers
from wrapper.courier import Courier
from wrapper.courier_login import CourierLogin


class TestCourierDelete:
    @allure.title('Тест успешного удаления курьера')
    @allure.description('Успешный запрос удаления курьера возвращает {"ok":true}')
    def test_delete_courier_correct_id_return_ok(self, create_courier_payload, login_courier_payload):
        Courier().create_new_courier(create_courier_payload)
        courier_id = CourierLogin().login_courier(login_courier_payload).json()['id']

        response = Courier().delete_courier(courier_id)

        assert (response.status_code == requests.codes['ok'] and
                response.json()['ok'] is True)

    @allure.title('Тест удаления курьера без указания id')
    @allure.description('Если отправить запрос без id, вернётся ошибка Not Found')
    def test_delete_courier_without_id_return_not_found_error(self):
        response = Courier().delete_courier("")

        assert (response.status_code == requests.codes["not_found"] and
                response.json()['message'] == 'Not Found.')

    @allure.title('Тест удаления курьера с несуществующим id')
    @allure.description('Если отправить запрос с несуществующим id, вернётся ошибка Not Found')
    def test_delete_courier_wrong_id_return_not_found_error(self):
        courier_id = helpers.random_id()
        response = Courier().delete_courier(courier_id)

        assert (response.status_code == requests.codes["not_found"] and
                response.json()['message'] == 'Курьера с таким id нет.')
