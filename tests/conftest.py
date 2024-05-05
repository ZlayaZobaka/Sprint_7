import pytest
import helpers
import copy

@pytest.fixture
def new_courier_payload():
    payload = {
        "firstName": helpers.generate_random_string(10),
        "login": helpers.generate_random_string(10),
        "password": helpers.generate_random_string(10)
    }
    yield payload
    del payload

@pytest.fixture
def login_courier_payload(new_courier_payload):
    payload = copy.copy(new_courier_payload)
    del payload["firstName"]
    yield payload
    del payload

