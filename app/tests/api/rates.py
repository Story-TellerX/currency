from currency import choices
from currency.models import Rate


def test_rates_list(client_api_auth):
    response = client_api_auth.get('/api/v1/rates/')
    assert response.status_code == 200
    assert 'results' in response.json()


def test_rates_create_invalid(client_api_auth):
    response = client_api_auth.post('/api/v1/rates/', data={})
    assert response.status_code == 400
    assert response.json() == {
        'type_curr': ['This field is required.'],
        'buy': ['This field is required.'],
        'sale': ['This field is required.']
    }


def test_rates_create_success(client_api_auth, bank):
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


def test_rates_update_invalid(client_api_auth, bank, test_rate_create_as_fixtures):
    data_update = {
        'buy': "25",
        'sale': 30,
        'type_curr': choices.RATE_TYPE_EUR,
        'bank': 99999,
    }
    response = client_api_auth.post('/api/v1/rates/', data=data_update)
    assert response.status_code == 400
    assert response.json() == {'bank': ['Invalid pk "99999" - object does not exist.']}


def test_rates_update_success(client_api_auth, bank, test_rate_create_as_fixtures):
    data_update = {
        'buy': 25,
        'sale': 30,
        'type_curr': choices.RATE_TYPE_EUR,
        'bank': bank.id,
    }
    response = client_api_auth.post('/api/v1/rates/', data=data_update)
    assert response.status_code == 201
    assert response.json() == {
        'id': 2,
        'type_curr': 1,
        'buy': '25.00',
        'sale': '30.00',
        'bank_object': {'id': 6,
                        'name': 'SkyBank',
                        'original_url': 'https://tascombank.ua/',
                        'number': '0 (800) 503 580'
                        }
    }


def test_rates_delete(client_api_auth):
    rates_initial_counts = Rate.objects.count()
    response = client_api_auth.delete('/api/v1/rates/1/')
    assert response.status_code == 204
    assert Rate.objects.count() == rates_initial_counts - 1
