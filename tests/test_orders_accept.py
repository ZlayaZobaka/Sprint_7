class OrdersAccept:
    # успешный запрос возвращает {"ok":true}
    def test_accept_order_correct_data_return_ok(self):
        pass

    # если передать неверный id курьера/заказа, запрос вернёт ошибку Not Found
    def test_accept_order_wrong_id_return_not_found_error(self):
        pass

    # если не передать id курьера/заказа, запрос вернёт ошибку Bad Request
    def test_accept_order_without_id_return_bad_request_error(self):
        pass