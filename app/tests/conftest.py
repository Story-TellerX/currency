import pytest
from django.core.management import call_command


@pytest.fixture(autouse=True, scope="function")
def enable_db_access_for_all_tests(db):
    """
    give access to database for all tests
    """


@pytest.fixture(autouse=True, scope="session")
def load_fixtures(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'app/tests/fixtures/banks.json')


@pytest.fixture()
def fake():
    from faker import Faker
    faker = Faker()
    yield faker


@pytest.fixture(scope="function")
def client_api_auth(django_user_model):
    from rest_framework.test import APIClient

    client = APIClient()
    email = "test12@test.com"
    password = "first-pass-1"

    user = django_user_model.objects.create(email=email, password=password)
    user.set_password(password)
    user.save()

    response = client.post('/api/v1/token/', data={
        'email': email,
        'password': password
    })
    assert response.status_code == 200

    client.credentials(HTTP_AUTHORIZATION='JWT ' + response.json()['access'])

    yield client

    user.delete()


@pytest.fixture(scope='function')
def bank(enable_db_access_for_all_tests):
    from currency.models import Bank

    yield Bank.objects.last()


@pytest.fixture()
def rate_create_as_fixtures(client_api_auth, bank):
    from currency import choices
    data = {
        'buy': 20,
        'sale': 21,
        'type_curr': choices.RATE_TYPE_USD,
        'bank': bank.id,
    }
    response = client_api_auth.post('/api/v1/rates/', data=data)
    assert response.status_code == 201
    assert response.json() == {
        'id': 1,
        'type_curr': 0,
        'buy': '20.00',
        'sale': '21.00',
        'bank_object': {'id': 6,
                        'name': 'SkyBank',
                        'original_url': 'https://tascombank.ua/',
                        'number': '0 (800) 503 580'
                        }
    }
