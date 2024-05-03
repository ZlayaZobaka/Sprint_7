class TestCourierDelete:
    # успешный запрос возвращает{"ok":true}
    def test_delete_courier_correct_id_return_ok(self):
        pass

    # если отправить запрос без id, вернётся ошибка Bad Request
    def test_delete_courier_without_id_return_bad_request_error(self):
        pass

    # если отправить запрос с несуществующим id, вернётся ошибка Not Found
    def test_delete_courier_wrong_id_return_not_found_error(self):
        pass
