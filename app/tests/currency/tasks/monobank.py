import json
from unittest.mock import MagicMock

from currency.models import Rate
from currency.tasks import parse_monobank


def test_parse_monobank(mocker):
    with open('app/tests/fixtures/mono_curr.json', 'r') as f:
        mono_curr_data = json.load(f)
    json_mock = lambda: mono_curr_data  # noqa
    requests_get = mocker.patch('requests.get', return_value=MagicMock(json=json_mock))  # noqa

    # I added full creating data for banks as data_fixtures

    initial_count = Rate.objects.count()

    parse_monobank()
    assert Rate.objects.count() == initial_count + 2

    parse_monobank()
    assert Rate.objects.count() == initial_count + 2
