import pytest
import helpers
import copy
from wrapper.courier import Courier
from wrapper.courier_login import CourierLogin
from wrapper.orders import Orders
from wrapper.orders_track import OrdersTrack

from faker import Faker


@pytest.fixture(scope='function')
def create_courier_payload():
    payload = {
        'firstName': helpers.generate_random_string(),
        'login': helpers.generate_random_string(),
        'password': helpers.generate_random_string()
    }
    return payload


@pytest.fixture(scope='function')
def create_bad_courier(request, create_courier_payload):
    create_courier_payload[request.param] = ''
    return create_courier_payload


@pytest.fixture(scope='function')
def login_courier_payload(create_courier_payload):
    payload = copy.copy(create_courier_payload)
    del payload['firstName']
    return payload


@pytest.fixture(scope='function')
def login_wrong_data_courier(request, login_courier_payload):
    payload = copy.copy(login_courier_payload)
    payload[request.param] = helpers.generate_random_string()
    return payload


@pytest.fixture(scope='function')
def login_empty_data_courier(request, login_courier_payload):
    payload = copy.copy(login_courier_payload)
    payload[request.param] = ''
    return payload


@pytest.fixture(scope='function')
def delete_courier(login_courier_payload):
    def _delete():
        response = CourierLogin().login_courier(login_courier_payload)
        courier_id = response.json()['id']
        Courier().delete_courier(courier_id)

    return _delete


@pytest.fixture(scope='function')
def create_order_payload(request):
    fake = Faker()
    payload = {
        'firstName': fake.name(),
        'lastName': fake.last_name(),
        'address': fake.address(),
        'metroStation': fake.random_int(1, 100),
        'phone': fake.phone_number(),
        'rentTime': fake.random_int(1, 10),
        'deliveryDate': fake.date(),
        'comment': fake.text(max_nb_chars=100),
        'color': request.param.split(',') if request.param_index > 0 else []
    }
    return payload


@pytest.fixture(scope='function')
def create_order_accept_payload(create_courier_payload, login_courier_payload, create_order_payload):
    Courier().create_new_courier(create_courier_payload)
    courier_id = CourierLogin().login_courier(login_courier_payload).json()['id']

    order_track = Orders().create_new_order(create_order_payload).json()['track']
    order_id = OrdersTrack().track_order(order_track).json()['order']['id']

    return [order_id, courier_id]
