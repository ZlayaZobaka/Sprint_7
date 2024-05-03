class OrdersTrack:
    # успешный запрос возвращает объект с заказом
    def test_track_order_correct_data_return_order_object(self):
        pass

    # запрос с несуществующим заказом возвращает ошибку Not Found
    def test_track_order_wrong_id_return_not_found_error(self):
        pass

    # запрос без номера заказа возвращает ошибку Bad Request
    def test_track_order_without_id_return_bad_request_error(self):
        pass