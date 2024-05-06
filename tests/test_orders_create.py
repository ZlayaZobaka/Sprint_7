import allure
import requests
import pytest
from wrapper.orders import Orders


class TestOrdersCreate:
    @allure.title('Тест создания заказа с разными вариантами цвета')
    @allure.description('Можно указать оба цвета/один из них/ни одного. Успешный запрос возвращает track')
    @pytest.mark.parametrize('create_order_payload', ('', 'BLACK', 'GREY', 'BLACK,GREY'), indirect=True)
    def test_create_order_set_color_return_track(self, create_order_payload):
        response = Orders().create_new_order(create_order_payload)

        assert (response.status_code == requests.codes['created'] and
                'track' in response.json())
