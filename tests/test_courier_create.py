import allure
import requests
import pytest
from wrapper.courier import Courier


class TestCourierCreate:
    # успешный запрос возвращает {"ok":true}
    def test_create_courier_correct_data_return_ok(self, create_courier_payload, delete_courier):
        response = Courier().create_new_courier(create_courier_payload)

        assert (response.status_code == requests.codes['created'] and
                response.json()['ok'] is True)

        delete_courier()

    # если создать пользователя с логином, который уже есть, возвращается ошибка Сonflict
    def test_create_courier_same_login_return_conflict_error(self, create_courier_payload, delete_courier):
        Courier().create_new_courier(create_courier_payload)
        response = Courier().create_new_courier(create_courier_payload)

        assert (response.status_code == requests.codes['conflict'] and
                response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.')

        delete_courier()

    # если одного из полей нет, запрос возвращает ошибку Bad Request
    @pytest.mark.parametrize('create_bad_courier', ('login', 'password'), indirect=True)
    def test_create_courier_empty_data_return_bad_request_error(self, create_bad_courier):
        response = Courier().create_new_courier(create_bad_courier)

        assert (response.status_code == requests.codes['bad_request'] and
                response.json()['message'] == 'Недостаточно данных для создания учетной записи')
