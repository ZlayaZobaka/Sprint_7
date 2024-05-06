import allure
import requests
from wrapper.orders import Orders


class TestOrdersGetAll:
    @allure.title('Тест получения списка заказов')
    @allure.description('В теле ответа возвращается список заказов')
    def test_order_get_all_return_orders_list(self):
        response = Orders().get_orders()

        assert (response.status_code == requests.codes['ok'] and
                len(response.json()['orders']) > 0)
