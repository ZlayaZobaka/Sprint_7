import allure
import requests
import helpers
from wrapper.orders import Orders
from wrapper.orders_track import OrdersTrack


class TestOrdersTrack:
    @allure.title('Тест получения заказа по его номеру')
    @allure.description('Успешный запрос возвращает объект с заказом')
    def test_track_order_correct_data_return_order_object(self, create_order_payload):
        order_track = Orders().create_new_order(create_order_payload).json()['track']

        response = OrdersTrack().track_order(order_track)

        assert (response.status_code == requests.codes['ok'] and
                'order' in response.json())

    @allure.title('Тест получения заказа с несуществующим номером')
    @allure.description('Запрос с несуществующим заказом возвращает ошибку Not Found')
    def test_track_order_wrong_id_return_not_found_error(self):
        random_order_track = helpers.random_id()

        response = OrdersTrack().track_order(random_order_track)

        assert (response.status_code == requests.codes['not_found'] and
                response.json()['message'] == "Заказ не найден")

    @allure.title('Тест получения заказа без его номера')
    @allure.description('Запрос без номера заказа возвращает ошибку Bad Request')
    def test_track_order_without_id_return_bad_request_error(self):
        response = OrdersTrack().track_order('')

        assert response.status_code == requests.codes['bad_request']
