from currency.models import Rate
from currency.tasks import parse_privatbank


def test_parse_privatbank():
    # Rate.objects.all().delete()

    # I added full creating data for banks as data_fixtures

    initial_count = Rate.objects.count()

    parse_privatbank()
    assert Rate.objects.count() == initial_count + 2

    parse_privatbank()
    assert Rate.objects.count() == initial_count + 2
