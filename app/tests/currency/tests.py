from django.conf import settings
import pytest
from currency import choices
from currency.models import Bank, Rate, ContactUs


def test_sanity_check():
    print(f'DEBUG {settings.DEBUG}')  # noqa
    assert 200 == 200


@pytest.mark.skip
def test_index_skip(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'index.html' in [t.name for t in response.templates]
    assert [t.name for t in response.templates] == [
        'index.html',
        'base.html',
        'includes/navbar.html',
        'includes/footer.html'
    ]


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'index.html' in [t.name for t in response.templates]
    assert [t.name for t in response.templates] == [
        'index.html',
        'base.html',
        'includes/navbar.html',
        'includes/footer.html'
    ]


def rate_list(client):
    response = client.get('/currency/rate/list/')
    assert response.status_code == 200


def test_create_rate_get_form(client):
    response = client.get('/currency/rate/create/')
    assert response.status_code == 200


def test_create_rate_empty_form(client):
    response = client.post('/currency/rate/create/')
    assert response.status_code == 200
    assert response.context['form'].errors == {
        'type_curr': ['This field is required.'],
        'buy': ['This field is required.'],
        'sale': ['This field is required.'],
        'bank': ['This field is required.']
    }


def test_create_rate_invalid_form(client):
    rates_initial_counts = Rate.objects.count()
    form_data = {
        'type_curr': choices.RATE_TYPE_USD,
        'buy': 20,
        'sale': 30,
        'bank': 99999
    }
    response = client.post('/currency/rate/create/', data=form_data)
    assert response.status_code == 200
    assert response.context['form'].errors == {
        'bank': ['Select a valid choice. That choice is not one of the available choices.']
    }
    assert Rate.objects.count() == rates_initial_counts


def test_create_rate_success(client):
    rates_initial_counts = Rate.objects.count()
    bank = Bank.objects.first()
    form_data = {
        'type_curr': choices.RATE_TYPE_USD,
        'buy': 20,
        'sale': 30,
        'bank': bank.id
    }
    response = client.post('/currency/rate/create/', data=form_data)
    assert response.status_code == 302
    assert response.url == '/currency/rate/list/'
    assert Rate.objects.count() == rates_initial_counts + 1


# @pytest.mark.skip('TODO not passed on CI')
def test_create_contactus(client, mailoutbox):
    contactus_initial_counts = ContactUs.objects.count()
    form_data = {
        'email_from': 'ds_ch@i.ua',
        'subject': "Topic fro subject",
        'message': 'Message'
    }
    response = client.post('/currency/contact-us/create/', data=form_data)
    assert response.status_code == 302
    assert ContactUs.objects.count() == contactus_initial_counts + 1
    assert response.url == '/currency/contactus/list/'
    assert len(mailoutbox) == 1
    mail = mailoutbox[0]
    assert mail.to == ['ds_ch@i.ua']
    assert mail.cc == []
    assert mail.bcc == []
    assert mail.reply_to == []
    # assert mail.from_email == settings.EMAIL_HOST_USER
