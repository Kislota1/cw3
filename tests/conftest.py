import pytest

@pytest.fixture
def test_data():
    return [
        {
            "id": 482520625,
            "state": "EXECUTED",
            "date": "2019-11-13T17:38:04.800051",
            "operationAmount": {
                "amount": "62814.53",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 38611439522855669794",
            "to": "Счет 46765464282437878125"
        },
    {
        "id": 15948212,
        "state": "EXECUTED",
        "date": "2018-12-23T11:47:52.403285",
        "operationAmount": {
            "amount": "47408.20",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "МИР 8665240839126074",
        "to": "Maestro 3000704277834087"
    },
    {
        "id": 114832369,
        "state": "EXECUTED",
        "date": "2019-12-07T06:17:14.634890",
        "operationAmount": {
            "amount": "48150.39",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Classic 2842878893689012",
        "to": "Счет 35158586384610753655"
    },
    {
        "id": 176798279,
        "state": "CANCELED",
        "date": "2019-04-18T11:22:18.800453",
        "operationAmount": {
            "amount": "73778.48",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 90417871337969064865"
    },
        {
            "id": 636137913,
            "state": "EXECUTED",
            "date": "2019-06-16T22:17:01.825020",
            "operationAmount": {
                "amount": "24260.78",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Platinum 8990850370884895",
            "to": "Счет 15574304810835774010"
        }
    ]
