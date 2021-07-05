from celery import shared_task
from django.core.mail import send_mail
import requests
from currency.utils import to_decimal


def _get_privatbank_currencies():
    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(url)
    response.raise_for_status()
    currencies = response.json()
    return currencies


@shared_task()
def parse_privatbank():
    from currency.models import Rate

    currencies = _get_privatbank_currencies()

    available_currencies_types = ('USD', 'EUR')

    source = 'privatbank'

    for curr in currencies:
        currencies_type = curr['ccy']
        if currencies_type in available_currencies_types:
            buy = to_decimal(curr['buy'])
            sale = to_decimal(curr['sale'])

            previous_rate = Rate.objects.filter(source=source, type_curr=currencies_type).order_by('created').last()

            if previous_rate is None or previous_rate.sale != sale or previous_rate.buy != buy:
                # previous_rate is None or  # Check for no exist rate
                # previous_rate.sale != sale or  # Check for changes related to last got data
                # previous_rate.buy != buy
                Rate.objects.create(
                    type_curr=currencies_type,
                    sale=sale,
                    buy=buy,
                    source=source,
                )


@shared_task(
    autoretry_for=(Exception,),
    retry_kwargs={
        'max_retries': 5,
        'default_retry_delay': 60,
    }
)
def send_email_background(body):
    send_mail(
        'New Contact Us form is created',
        body,
        'testtestapp454545@gmail.com',
        ['ds_ch@i.ua'],
        fail_silently=False,
    )


@shared_task()
def print_hello_world_beat():
    print('BEAT')  # noqa
