class HTTPStatusCodes:

    CODE_200_OK = {
        'status_code': 200,
        'message': {'ok': True}
    }

    CODE_201_CREATED = {
        'status_code': 201,
        'message': {'ok': True}
    }

    CREATE_COURIER_CODE_400_BAD_REQUEST = {
        'status_code': 400,
        'message': 'Недостаточно данных для создания учетной записи'
    }

    CREATE_COURIER_CODE_409_CONFLICT = {
        'status_code': 409,
        'message': 'Этот логин уже используется'
    }

    LOGIN_COURIER_CODE_400_BAD_REQUEST = {
        'status_code': 400,
        'message': 'Недостаточно данных для входа'
    }

    LOGIN_COURIER_CODE_404_NOT_FOUND = {
        'status_code': 404,
        'message': 'Учетная запись не найдена'
    }
