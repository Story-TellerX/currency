from unittest.mock import MagicMock

from currency.models import Rate
from currency.tasks import parse_privatbank


def test_parse_privatbank(mocker):
    json_mock = lambda: [  # noqa
        {"ccy": "USD", "base_ccy": "UAH", "buy": "26.75000", "sale": "27.15000"},
        {"ccy": "EUR", "base_ccy": "UAH", "buy": "31.50000", "sale": "32.10000"},
        {"ccy": "RUR", "base_ccy": "UAH", "buy": "0.35500", "sale": "0.38500"},
        {"ccy": "BTC", "base_ccy": "USD", "buy": "36280.7311", "sale": "40099.7555"}
    ]
    requests_get = mocker.patch('requests.get', return_value=MagicMock(json=json_mock))  # noqa

    # I added full creating data for banks as data_fixtures

    initial_count = Rate.objects.count()

    parse_privatbank()
    assert Rate.objects.count() == initial_count + 2

    parse_privatbank()
    assert Rate.objects.count() == initial_count + 2
