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


def _get_monobank_currencies():
    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    response.raise_for_status()
    currencies = response.json()
    return currencies


@shared_task()
def parse_monobank():
    from currency.models import Rate
    currencies = _get_monobank_currencies()

    available_currencies_raw = (840, 978)
    second_type_curr = (980)
    available_currencies_normal = {
        840: 'USD',
        978: 'EUR',
    }
    source = 'monobank'
    for curr in currencies:
        currencies_type = curr['currencyCodeA']
        second_pair_currencies_type = curr['currencyCodeB']
        if currencies_type in available_currencies_raw and second_pair_currencies_type == second_type_curr:
            type_curr = curr['currencyCodeA']
            type_curr_norm = available_currencies_normal[type_curr]
            buy = to_decimal(curr['rateBuy'])
            sale = to_decimal(curr['rateSell'])

            previous_rate = Rate.objects.filter(source=source, type_curr=type_curr_norm).order_by('created').last()

            if previous_rate is None or previous_rate.sale != sale or previous_rate.buy != buy:

                Rate.objects.create(
                    type_curr=type_curr_norm,
                    sale=sale,
                    buy=buy,
                    source=source,
                )


@shared_task()
def parse_vkurse():
    from currency.models import Rate
    url = 'http://vkurse.dp.ua/course.json'
    response = requests.get(url)
    response.raise_for_status()
    currencies = response.json()
    available_currencies_types = ('Dollar', 'Euro')
    source = 'vkurse'
    available_currencies_normal = {
        'Dollar': 'USD',
        'Euro': 'EUR',
    }
    for key, value in currencies.items():
        if key in available_currencies_types:
            type_curr_norm = available_currencies_normal[key]
            buy = to_decimal(value.get('buy'))
            sale = to_decimal(value.get('sale'))

            previous_rate = Rate.objects.filter(source=source, type_curr=type_curr_norm).order_by('created').last()

            if previous_rate is None or previous_rate.sale != sale or previous_rate.buy != buy:

                Rate.objects.create(
                    type_curr=type_curr_norm,
                    sale=sale,
                    buy=buy,
                    source=source,
                )


def _get_otp_bunk_currencies():
    url = 'https://ru.otpbank.com.ua/local/components/otp/utils.exchange_rate_smart/exchange_rate_by_date.php?' \
          'curr_date=07.07.2021&ib_code=otpb_banking_exchange_rates'
    response = requests.get(url)
    response.raise_for_status()
    currencies = response.json()
    return currencies


@shared_task()
def parse_otp_bank():
    from currency.models import Rate

    currencies = _get_otp_bunk_currencies()
    currencies_value = currencies.get('items')

    available_currencies_types = ('USD', 'EUR')
    second_type_curr = ('UAH')

    source = 'otp bank'

    for curr in currencies_value:
        currencies_type = curr['NAME']
        second_pair_currencies_type = curr['CHANGE']
        if currencies_type in available_currencies_types and second_pair_currencies_type == second_type_curr:
            buy = to_decimal(curr['BUY'])
            sale = to_decimal(curr['SELL'])

            previous_rate = Rate.objects.filter(source=source, type_curr=currencies_type).order_by('created').last()

            if previous_rate is None or previous_rate.sale != sale or previous_rate.buy != buy:
                Rate.objects.create(
                    type_curr=currencies_type,
                    sale=sale,
                    buy=buy,
                    source=source,
                )


def _get_iboxbunk_currencies():
    url = 'https://app.iboxbank.online/api/currency/rate-only-base/UAH'
    response = requests.get(url)
    currencies = response.json()
    currencies_data = currencies['rate']
    return currencies_data


@shared_task()
def parse_iboxbank():
    from currency.models import Rate

    currencies = _get_iboxbunk_currencies()

    available_currencies_type = ('USD', 'EUR')
    source = 'iboxbank'

    for curr in currencies:
        currencies_type = curr['currency']
        if currencies_type in available_currencies_type:
            buy = to_decimal(curr['buyValue'])
            sale = to_decimal(curr['saleValue'])

            previous_rate = Rate.objects.filter(source=source, type_curr=currencies_type).order_by('created').last()

            if previous_rate is None or previous_rate.sale != sale or previous_rate.buy != buy:
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
