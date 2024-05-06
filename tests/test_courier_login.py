import allure
import requests
import pytest
from wrapper.courier import Courier
from wrapper.courier_login import CourierLogin


class TestCourierLogin:
    @allure.title('Тест успешной авторизации курьера')
    @allure.description('Успешный запрос на авторизацию курьера возвращает id')
    def test_login_courier_correct_data_return_id(
            self, create_courier_payload, login_courier_payload, delete_courier):
        Courier().create_new_courier(create_courier_payload)
        response = CourierLogin().login_courier(login_courier_payload)

        assert (response.status_code == requests.codes['ok'] and
                'id' in response.json())

        delete_courier()

    @allure.title('Тест авторизации курьера с неправильным логином/паролем')
    @allure.description('Если неправильно указать логин или пароль запрос возвращает ошибку Not Found')
    @pytest.mark.parametrize('login_wrong_data_courier', ('login', 'password'), indirect=True)
    def test_login_courier_wrong_data_return_not_found_error(
            self, create_courier_payload, login_wrong_data_courier, delete_courier):
        Courier().create_new_courier(create_courier_payload)
        response = CourierLogin().login_courier(login_wrong_data_courier)

        assert (response.status_code == requests.codes['not_found'] and
                response.json()['message'] == 'Учетная запись не найдена')

        delete_courier()

    @allure.title('Тест авторизации курьера, если отсутствует часть обязательных полей')
    @allure.description('Если одного из полей нет, запрос возвращает ошибку Bad Request')
    @pytest.mark.parametrize('login_empty_data_courier', ('login', 'password'), indirect=True)
    def test_login_courier_empty_data_return_bad_request_error(
            self, create_courier_payload, login_empty_data_courier, delete_courier):
        Courier().create_new_courier(create_courier_payload)
        response = CourierLogin().login_courier(login_empty_data_courier)

        assert (response.status_code == requests.codes['bad_request'] and
                response.json()['message'] == 'Недостаточно данных для входа')

        delete_courier()
