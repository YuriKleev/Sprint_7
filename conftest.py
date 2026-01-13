import requests
import pytest

import random
import string

from endpoints import *
from data import TestData
from methods import Methods

@pytest.fixture(scope="function")
def new_courier_data():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login=generate_random_string(10)
    password=generate_random_string(10)
    first_name=generate_random_string(10)

    courier_data={
        'login': login,
        'password': password,
        'firstName': first_name
    }

    yield courier_data

    Methods.delete_courier(courier_data["login"], courier_data["password"])


@pytest.fixture(scope="function")
def courier_with_valid_data():
    courier_data = TestData.COURIER_DATA.copy()

    yield courier_data

    Methods.delete_courier(courier_data["login"], courier_data["password"])
