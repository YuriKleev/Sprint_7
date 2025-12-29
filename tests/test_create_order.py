import pytest
import allure

from methods import Methods
from data import TestData
from status_codes import HTTPStatusCodes

class TestCreateOrder:

    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    @allure.title("Проверка возможности создания заказа")
    def test_create_order_success(self, color):
        allure.dynamic.description(
            f"Проверяем создание заказа. Выбран цвет самоката: {color}." 
            f"Ожидаемый результат: код 201 Created"
        )
        order_data = TestData.ORDER_DATA.copy()
        order_data["color"] = color
        response = Methods.make_order(order_data)
        assert response.status_code == HTTPStatusCodes.CODE_201_CREATED['status_code']
        assert 'track' in response.json()

        Methods.cancel_order(response.status_code, response.json()["track"])
