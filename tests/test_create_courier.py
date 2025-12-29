import pytest
import allure

from conftest import new_courier_data, courier_with_valid_data

from methods import Methods
from data import TestData
from status_codes import HTTPStatusCodes


class TestCreateCourier:

    @allure.title("Проверка возможности создания курьера")
    @allure.description(
        f"Проверяем успешное создание курьера с валидными данными"
        f"Ожидаемый результат: код 201 Created"
    )
    def test_create_courier_success(self, new_courier_data):
            response = Methods.create_courier(new_courier_data)
            assert response.status_code == HTTPStatusCodes.CODE_201_CREATED['status_code']
            assert response.json() == HTTPStatusCodes.CODE_201_CREATED['message']


    @allure.title("Проверка невозможности создания двух курьеров с одинаковыми данными")
    @allure.description(
        f"Проверяем,что при попытке создать курьера с логином, который уже есть, возвращается ошибка"
        f"Ожидаемый результат: код 409 Conflict"
    )
    def test_create_two_same_couriers_failed(self, courier_with_valid_data):
            first_courier_response = Methods.create_courier(courier_with_valid_data)
            second_courier_response = Methods.create_courier(courier_with_valid_data)
            assert second_courier_response.status_code == HTTPStatusCodes.CREATE_COURIER_CODE_409_CONFLICT['status_code']
            assert second_courier_response.json()['message'] == HTTPStatusCodes.CREATE_COURIER_CODE_409_CONFLICT['message']
 

    @pytest.mark.parametrize('empty_field', ['login', 'password']) 
    @allure.title(
        f"Проверка возвращения ошибки при создании курьера с незаполненными обязательными полями"
        f"Ожидаемый результат: код 400 Bad Request"
    )
    def test_create_courier_with_empty_fields_failed(self, courier_with_valid_data, empty_field):
        allure.dynamic.description(f"Проверяем,что при попытке создать курьера с незаполненным полем {empty_field} возвращается ошибка")
        courier_data = courier_with_valid_data
        courier_data[empty_field] = ''
        response = Methods.create_courier(courier_data)
        assert response.status_code == HTTPStatusCodes.CREATE_COURIER_CODE_400_BAD_REQUEST['status_code']
        assert response.json()['message'] == HTTPStatusCodes.CREATE_COURIER_CODE_400_BAD_REQUEST['message']
