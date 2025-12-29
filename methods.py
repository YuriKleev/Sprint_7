import requests
import allure
from endpoints import *

from status_codes import HTTPStatusCodes

class Methods:

    @staticmethod
    @allure.step('Отправка POST-запроса для создания курьера')
    def create_courier(payload):
        return requests.post(url=Endpoints.CREATE_COURIER_ENDPOINT, data=payload)

    @staticmethod
    @allure.step('Отправка POST-запроса для авторизации курьера')
    def login_courier(login, password):
        payload = {
            'login': login,
            'password': password
        }
        return requests.post(url=Endpoints.LOGIN_COURIER_ENDPOINT, data=payload)

    @staticmethod
    @allure.step('Отправка POST-запроса для создания заказа')
    def make_order(payload):
        return requests.post(url=Endpoints.MAKE_ORDER_ENDPOINT, data=payload)

    @staticmethod
    @allure.step('Отправка GET-запроса для получения списка заказов')
    def get_orders_list():
        return requests.get(url=Endpoints.GET_ORDERS_LIST_ENDPOINT)

    @staticmethod
    @allure.step("Отправка DELETE-запроса для удаления курьера")
    def delete_courier(login, password):
        response = Methods.login_courier(login, password)
        if response.status_code == HTTPStatusCodes.CODE_200_OK:
            courier_id = response.json()["id"]
            requests.delete(url=f'{Endpoints.DELETE_COURIER_ENDPOINT}/{courier_id}')

    @staticmethod
    @allure.title("Отправка PUT-запроса для отмены заказа")
    def cancel_order(status_code, track):
        if status_code == HTTPStatusCodes.CODE_200_OK:
            requests.put(url=Endpoints.CANCEL_ORDER_ENDPOINT, body={"track": track})
