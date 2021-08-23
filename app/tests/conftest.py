import pytest
from django.core.management import call_command
from django.db.models import signals

from accounts.models import User
from accounts.signals import (
    user_deleting_is_denied,
    pre_save_profile_phone,
    pre_save_profile_email,
    post_save_user_send_to_cool_service,
    post_save_user_send_to_awesome_service,
)


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
    email = "admin@admin.com"
    password = "admin@admin.com"
    phone = '847259'

    user = django_user_model.objects.create(email=email, password=password, phone=phone)
    user.set_password(password)

    signals.pre_save.disconnect(pre_save_profile_phone, sender=User)
    signals.pre_save.disconnect(pre_save_profile_email, sender=User)

    user.save()

    signals.post_save.disconnect(post_save_user_send_to_cool_service, sender=User)
    signals.post_save.disconnect(post_save_user_send_to_awesome_service, sender=User)

    response = client.post('/api/v1/token/', data={
        'email': email,
        'password': password
    })
    assert response.status_code == 200

    client.credentials(HTTP_AUTHORIZATION='JWT ' + response.json()['access'])

    yield client

    signals.pre_delete.disconnect(user_deleting_is_denied, sender=User)

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
