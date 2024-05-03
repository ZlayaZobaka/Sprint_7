class CourierLogin:
    # курьер может авторизоваться, успешный запрос возвращает id
    def test_login_courier_correct_data_return_id(self):
        pass

    # если неправильно указать логин или пароль запрос возвращает ошибку Not Found
    def test_login_courier_wrong_data_return_not_found_error(self):
        pass

    # если какого-то поля нет, запрос возвращает ошибку Bad Request
    def test_login_courier_incorrect_data_bad_request_error(self):
        pass
