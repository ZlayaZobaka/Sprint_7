import pytest
from wrapper.courier import Courier
from wrapper.courier_login import CourierLogin


class TestCourierLogin:
    # курьер может авторизоваться, успешный запрос возвращает id
    def test_login_courier_correct_data_return_id(self):
        courier = Courier()
        payload = courier.create_new_courier_payload()
        courier.create_new_courier(payload)
        courier_login = CourierLogin()
        login_payload = courier_login.login_courier_payload(payload)

        response = courier_login.login_courier(login_payload)

        assert (response.status_code == 200 and
                'id' in response.json())

    # если неправильно указать логин или пароль запрос возвращает ошибку Not Found
    def test_login_courier_wrong_data_return_not_found_error(self):
        pass

    # если какого-то поля нет, запрос возвращает ошибку Bad Request
    @pytest.mark.parametrize(
        "login, password",
        [
            [False, True],
            [True, False]
        ]
    )
    def test_login_courier_incorrect_data_bad_request_error(self, login, password):
        courier = Courier()
        payload = courier.create_new_courier_payload()
        courier.create_new_courier(payload)
        courier_login = CourierLogin()
        login_payload = courier_login.login_courier_payload(payload, login=login, password=password)

        response = courier_login.login_courier(login_payload)

        assert (response.status_code == 400 and
                response.json()['message'] == 'Недостаточно данных для входа')
