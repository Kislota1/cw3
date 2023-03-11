import pytest

from tests.conftest import test_data
from utils import get_data, get_last_data, get_formatted_data, get_filtered_data


def test_get_data():
    url = 'https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1678636611553&signature=kuY0dGryrWwM41y666NrynudAisC3mUUmUOHn9zzo3Q&downloadName=operations.json'
    assert get_data(url)

def test_get_last_data(test_data):
    data = get_last_data(test_data, count_last_values=2)
    assert data[0]['date'] == '2019-12-07T06:17:14.634890'
    assert len(data) == 2

def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data[:1])
    assert data == ['13.11.2019 Перевод со счета на счет\nСчет 3861 14 ** **** 9794 -> Счет **8125\n62814.53 руб.\n']
    data = get_formatted_data(test_data[1:2])
    assert data == ['23.12.2018 Перевод с карты на карту\nМИР 8665 24 ** **** 6074 -> Счет **4087\n47408.20 USD\n']

def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data)) == 3
    assert len(get_filtered_data(test_data, filtered_empty_from=True)) == 3
