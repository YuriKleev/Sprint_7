import pytest
import allure

from conftest import new_courier_data

from methods import Methods
from status_codes import HTTPStatusCodes

class TestLoginCourier:

    @allure.title("Проверка возможности авторизации курьера")
    @allure.description(
        f"Проверяем успешной авторизации курьера с валидными данными"
        f"Ожидаемый результат: код 200 OK"
    )
    def test_login_courier_success(self, new_courier_data):
            Methods.create_courier(new_courier_data)
            response = Methods.login_courier(new_courier_data['login'], new_courier_data['password'])
            assert response.status_code == HTTPStatusCodes.CODE_200_OK['status_code']
            assert 'id' in response.json()


    @pytest.mark.parametrize('empty_field', ['login', 'password'])
    @allure.title(
        f"Проверка возвращения ошибки при авторизации курьера с незаполненными обязательными полями"
        f"Ожидаемый результат: код 400 Bad Request"
    )
    def test_login_courier_with_empty_fields_failed(self, new_courier_data, empty_field):
        allure.dynamic.description(f"Проверяем, что при авторизации курьера с незаполненным полем {empty_field} возвращается ошибка")
        courier_data = new_courier_data
        courier_data[empty_field] = ''
        response = Methods.login_courier(courier_data['login'], courier_data['password'])
        assert response.status_code == HTTPStatusCodes.LOGIN_COURIER_CODE_400_BAD_REQUEST['status_code']
        assert response.json()['message'] == HTTPStatusCodes.LOGIN_COURIER_CODE_400_BAD_REQUEST['message']

    @pytest.mark.parametrize('field', ['login', 'password'])
    @allure.title(
        f"Проверка возвращения ошибки при авторизации курьера с неправильно заполненным логином или паролем"
        f"Ожидаемый результат: код 404 Not Found"
    )
    def test_login_courier_with_wrong_fields_failed(self, new_courier_data, field):
        allure.dynamic.description(f"Проверяем, что при попытке авторизации курьера с неправильно заполненным полем {field} возвращается ошибка")
        courier_data = new_courier_data
        courier_data[field] = f"wrong{field}"
        response = Methods.login_courier(courier_data['login'], courier_data['password'])
        assert response.status_code == HTTPStatusCodes.LOGIN_COURIER_CODE_404_NOT_FOUND['status_code']
        assert response.json()['message'] == HTTPStatusCodes.LOGIN_COURIER_CODE_404_NOT_FOUND['message']


    @allure.title("Проверка невозможности авторизации несуществующего курьера")
    @allure.description(
        f"Проверка, что при авторизации несуществующего курьера возвращается ошибка"
        f"Ожидаемый результат: код 404 Not Found"
    )
    def test_login_nonexisting_courier_failed(self, new_courier_data):
        response = Methods.login_courier(new_courier_data['login'], new_courier_data['password'])
        assert response.status_code == HTTPStatusCodes.LOGIN_COURIER_CODE_404_NOT_FOUND['status_code']
        assert response.json()['message'] == HTTPStatusCodes.LOGIN_COURIER_CODE_404_NOT_FOUND['message']
