import pytest
from wrapper.courier import Courier


class TestCourierCreate:
    # успешный запрос возвращает {"ok":true}
    def test_create_courier_correct_data_return_ok(self):
        courier = Courier()
        payload = courier.create_new_courier_payload()

        response = courier.create_new_courier(payload)

        assert response.status_code == 201 and response.text == '{"ok":true}'

    # если создать пользователя с логином, который уже есть, возвращается ошибка Сonflict
    def test_create_courier_same_login_return_conflict_error(self):
        courier = Courier()
        payload = courier.create_new_courier_payload()

        courier.create_new_courier(payload)
        new_response = courier.create_new_courier(payload)

        assert (new_response.status_code == 409 and
                new_response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.')

    # если одного из полей нет, запрос возвращает ошибку Bad Request
    @pytest.mark.parametrize(
        "login, password",
        [
            [False, True],
            [True, False]
        ]
    )
    def test_create_courier_lack_data_return_bad_request_error(self, login, password):
        courier = Courier()
        payload = courier.create_new_courier_payload(login=login, password=password)

        response = courier.create_new_courier(payload)

        assert (response.status_code == 400 and
                response.json()['message'] == 'Недостаточно данных для создания учетной записи')
