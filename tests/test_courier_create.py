class TestCourierCreate:
    # успешный запрос возвращает {"ok":true}
    def test_create_courier_correct_data_return_ok(self):
        pass

    # если создать пользователя с логином, который уже есть, возвращается ошибка Сonflict
    def test_create_courier_same_login_return_conflict_error(self):
        pass

    # если одного из полей нет, запрос возвращает ошибку Bad Request
    def test_create_courier_lack_data_return_bad_request_error(self):
        pass