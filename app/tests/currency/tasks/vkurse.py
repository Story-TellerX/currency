from unittest.mock import MagicMock

from currency.models import Rate
from currency.tasks import parse_vkurse


def test_parse_vkurse(mocker):
    json_mock = lambda: {  # noqa
            "Dollar": {
                "buy": "26.85",
                "sale": "27.00"
            },
            "Euro": {
                "buy": "31.80",
                "sale": "31.95"
            },
            "Rub": {
                "buy": "0.363",
                "sale": "0.368"
            }
        }
    requests_get = mocker.patch('requests.get', return_value=MagicMock(json=json_mock))  # noqa

    # I added full creating data for banks as data_fixtures

    initial_count = Rate.objects.count()

    parse_vkurse()
    assert Rate.objects.count() == initial_count + 2

    parse_vkurse()
    assert Rate.objects.count() == initial_count + 2
