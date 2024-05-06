import allure
import requests
import pytest

import helpers
from wrapper.orders_accept import OrdersAccept


class TestOrdersAccept:
    # успешный запрос возвращает {"ok":true}
    def test_accept_order_correct_data_return_ok(
            self, create_order_accept_payload, delete_courier):
        response = OrdersAccept().accept_orders(*create_order_accept_payload)

        assert (response.status_code == requests.codes['ok'] and
                response.json()['ok'] is True)

        delete_courier()

    # если передать неверный id курьера/заказа, запрос вернёт ошибку Not Found
    @pytest.mark.parametrize("parameter_number", [x for x in range(0, 2)])
    def test_accept_order_wrong_id_return_not_found_error(
            self, parameter_number, create_order_accept_payload, delete_courier):
        create_order_accept_payload[parameter_number] = helpers.random_id()

        response = OrdersAccept().accept_orders(*create_order_accept_payload)

        assert response.status_code == requests.codes['not_found']

        delete_courier()

    # если не передать id курьера, запрос вернёт ошибку Bad Request
    def test_accept_order_wo_courier_id_return_bad_request_error(
            self, create_order_accept_payload, delete_courier):
        create_order_accept_payload[1] = ""

        response = OrdersAccept().accept_orders(*create_order_accept_payload)

        assert (response.status_code == requests.codes['bad_request'] and
                response.json()['message'] == "Недостаточно данных для поиска")

        delete_courier()

    # если не передать id заказа, запрос вернёт ошибку Not Found
    def test_accept_order_wo_order_id_return_bad_request_error(
            self, create_order_accept_payload, delete_courier):
        create_order_accept_payload[0] = ""

        response = OrdersAccept().accept_orders(*create_order_accept_payload)

        assert response.status_code == requests.codes['not_found']

        delete_courier()
