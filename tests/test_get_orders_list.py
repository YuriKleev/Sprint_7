import allure

from methods import Methods
from status_codes import HTTPStatusCodes

class TestGetOrdersList:

    @allure.title("Получение списка заказов")
    @allure.description(
        f"Проверка наличия списка заказов в теле ответа."
        f"Ожидаемый результат: код 200 ОК"
    )
    def test_get_orders_list(self):
        response = Methods.get_orders_list()
        assert response.status_code == HTTPStatusCodes.CODE_200_OK['status_code']
        assert 'orders' in response.json()
