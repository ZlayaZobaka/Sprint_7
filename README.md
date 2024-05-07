# Финальный проект Sprint_7 "Автотесты API учебного сервиса Яндекс Самокат"

## Описание тестов
- **test\test_courier_create.py** - тесты на создание курьера
- **test\test_courier_delete.py** - тесты на удаление курьера
- **test\test_courier_login.py** - тесты на авторизацию курьера
- **test\test_orders_accept.py** - тесты на принятие заказа
- **test\test_orders_create.py**  - тесты на создание заказа
- **test\test_orders_get_all.py** - тесты на получение списка заказов
- **test\test_orders_track.py** - тесты на получение заказа по его номеру

### вспомогательные файлы
- **wrapper\\*.py** - прокладки для взаимодействия с Requests HTTP Library
- **.gitignore** - список игнорироемых файлов в Git
- **conftest.py** - фикстуры
- **data.py** - статические данные тестов
- **helpers.py** - вспомогательные функции тестов
- **README.md** - описание проекта

# Запуск тестов
```sh
python -m pytest  
```