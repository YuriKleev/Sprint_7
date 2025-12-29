MAIN_PAGE_URL='https://qa-scooter.praktikum-services.ru'

class Endpoints:

    CREATE_COURIER_ENDPOINT = f'{MAIN_PAGE_URL}/api/v1/courier'
    LOGIN_COURIER_ENDPOINT = f'{MAIN_PAGE_URL}/api/v1/courier/login'
    DELETE_COURIER_ENDPOINT = f'{MAIN_PAGE_URL}/api/v1/courier'
    MAKE_ORDER_ENDPOINT = f'{MAIN_PAGE_URL}/api/v1/orders'
    GET_ORDERS_LIST_ENDPOINT = f'{MAIN_PAGE_URL}/api/v1/orders'
    CANCEL_ORDER_ENDPOINT = f'{MAIN_PAGE_URL}/api/v1/orders/cancel'
