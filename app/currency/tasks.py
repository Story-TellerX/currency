from celery import shared_task
from django.core.mail import send_mail
import requests
from currency.utils import to_decimal
from currency import choices, consts
from django.core.cache import cache


def _get_privat_and_mono_currencies(url):
    response = requests.get(url)
    response.raise_for_status()
    currencies = response.json()
    return currencies


@shared_task()
def parse_privatbank():
    from currency.models import Rate, Bank

    bank = Bank.objects.get(code_name=consts.CODE_NAME_PRIVATBANK)
    currencies = _get_privat_and_mono_currencies(bank.url)

    available_currencies_types = {
        'USD': choices.RATE_TYPE_USD,
        'EUR': choices.RATE_TYPE_EUR,
    }

    clear_cache = False

    for curr in currencies:
        currencies_type = curr['ccy']
        if currencies_type in available_currencies_types:
            currencies_type = available_currencies_types[curr['ccy']]
            buy = to_decimal(curr['buy'])
            sale = to_decimal(curr['sale'])

            previous_rate = Rate.objects.filter(bank=bank, type_curr=currencies_type).order_by('created').last()

            if previous_rate is None or previous_rate.sale != sale or previous_rate.buy != buy:
                # previous_rate is None or  # Check for no exist rate
                # previous_rate.sale != sale or  # Check for changes related to last got data
                # previous_rate.buy != buy
                Rate.objects.create(
                    type_curr=currencies_type,
                    sale=sale,
                    buy=buy,
                    bank=bank,
                )
                clear_cache = True

    if clear_cache:
        cache.delete(consts.CACHE_KEY_LATEST_RATES)


@shared_task()
def parse_monobank():
    from currency.models import Rate, Bank
    bank = Bank.objects.get(code_name=consts.CODE_NAME_MONOBANK)
    currencies = _get_privat_and_mono_currencies(bank.url)

    # available_currencies_raw = (840, 978)
    available_currencies_raw = {
        840: choices.RATE_TYPE_USD,
        978: choices.RATE_TYPE_EUR,
    }
    second_type_curr = 980
    # available_currencies_normal = {
    #     840: choices.RATE_TYPE_USD,
    #     978: choices.RATE_TYPE_EUR,
    # }
    for curr in currencies:
        currencies_type = curr['currencyCodeA']
        second_pair_currencies_type = curr['currencyCodeB']
        if currencies_type in available_currencies_raw and second_pair_currencies_type == second_type_curr:
            type_curr = available_currencies_raw[curr['currencyCodeA']]
            # type_curr_norm = available_currencies_normal[type_curr]
            buy = to_decimal(curr['rateBuy'])
            sale = to_decimal(curr['rateSell'])

            previous_rate = Rate.objects.filter(bank=bank, type_curr=type_curr).order_by('created').last()

            if previous_rate is None or previous_rate.sale != sale or previous_rate.buy != buy:

                Rate.objects.create(
                    type_curr=type_curr,
                    sale=sale,
                    buy=buy,
                    bank=bank,
                )


@shared_task()
def parse_vkurse():
    from currency.models import Rate, Bank
    bank = Bank.objects.get(code_name=consts.CODE_NAME_VKURSE)
    response = requests.get(bank.url)
    response.raise_for_status()
    currencies = response.json()
    available_currencies_types = {
        'Dollar': choices.RATE_TYPE_USD,
        'Euro': choices.RATE_TYPE_EUR,
    }
    # available_currencies_normal = {
    #     'Dollar': choices.RATE_TYPE_USD,
    #     'Euro': choices.RATE_TYPE_EUR,
    # }
    for key, value in currencies.items():
        if key in available_currencies_types:
            type_curr_norm = available_currencies_types[key]
            buy = to_decimal(value.get('buy'))
            sale = to_decimal(value.get('sale'))

            previous_rate = Rate.objects.filter(bank=bank, type_curr=type_curr_norm).order_by('created').last()

            if previous_rate is None or previous_rate.sale != sale or previous_rate.buy != buy:

                Rate.objects.create(
                    type_curr=type_curr_norm,
                    sale=sale,
                    buy=buy,
                    bank=bank,
                )


def _get_iboxbunk_currencies(url):
    response = requests.get(url)
    response.raise_for_status()
    currencies = response.json()
    currencies_data = currencies['rate']
    return currencies_data


@shared_task()
def parse_iboxbank():
    from currency.models import Rate, Bank
    bank = Bank.objects.get(code_name=consts.CODE_NAME_IBOX)

    currencies = _get_iboxbunk_currencies(bank.url)

    available_currencies_type = {
        'USD': choices.RATE_TYPE_USD,
        'EUR': choices.RATE_TYPE_EUR,
    }
    for curr in currencies:
        currencies_type = curr['currency']
        if currencies_type in available_currencies_type:
            currencies_type = available_currencies_type[curr['currency']]
            buy = to_decimal(curr['buyValue'])
            sale = to_decimal(curr['saleValue'])

            previous_rate = Rate.objects.filter(bank=bank, type_curr=currencies_type).order_by('created').last()

            if previous_rate is None or previous_rate.sale != sale or previous_rate.buy != buy:
                Rate.objects.create(
                    type_curr=currencies_type,
                    sale=sale,
                    buy=buy,
                    bank=bank,
                )


def _get_grant_currencies(url):
    response = requests.get(url)
    response.raise_for_status()
    currencies = response.json()
    return currencies


@shared_task()
def parse_grant():
    from currency.models import Rate, Bank
    bank = Bank.objects.get(code_name=consts.CODE_NAME_GRANT)
    currencies = _get_grant_currencies(bank.url)

    available_currencies_types = ('USD', 'EUR')
    available_currencies_normal = {
        '840': choices.RATE_TYPE_USD,
        '978': choices.RATE_TYPE_EUR,
    }

    for key, value in currencies.items():
        if key in available_currencies_types:
            type_curr_norm = available_currencies_normal[value.get('cur_ref')]
            buy = to_decimal(value.get('k_buy'))
            sale = to_decimal(value.get('k_sale'))

            previous_rate = Rate.objects.filter(bank=bank, type_curr=type_curr_norm).order_by('created').last()

            if previous_rate is None or previous_rate.sale != sale or previous_rate.buy != buy:

                Rate.objects.create(
                    type_curr=type_curr_norm,
                    sale=sale,
                    buy=buy,
                    bank=bank,
                )


def _get_sky_currencies(url):
    response = requests.get(url)
    response.raise_for_status()
    currencies = response.json()
    currencies_curr = currencies[0]
    all_elements_of_the_list = dict(enumerate(currencies_curr))
    return all_elements_of_the_list


@shared_task()
def parse_skybank():
    from currency.models import Rate, Bank
    bank = Bank.objects.get(code_name=consts.CODE_NAME_SKY)

    currencies = _get_sky_currencies(bank.url)

    available_currencies_type = {
        'USD': choices.RATE_TYPE_USD,
        'EUR': choices.RATE_TYPE_EUR,
    }
    type_for_curr_real = 'exchange'

    for key, value in currencies.items():
        exchange_id = value.get('kurs_type')
        short_name = value.get('short_name')
        if exchange_id in type_for_curr_real and short_name in available_currencies_type:
            name_for_curr = available_currencies_type[value.get('short_name')]
            buy = to_decimal(value.get('kurs_buy'))
            sale = to_decimal(value.get('kurs_sale'))

            previous_rate = Rate.objects.filter(bank=bank, type_curr=name_for_curr).order_by('created').last()

            if previous_rate is None or previous_rate.sale != sale or previous_rate.buy != buy:
                Rate.objects.create(
                    type_curr=name_for_curr,
                    sale=sale,
                    buy=buy,
                    bank=bank,
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


@shared_task(
    autoretry_for=(Exception,),
    retry_kwargs={
        'max_retries': 5,
    }
)
def send_email_from_api_background(body):
    send_mail(
        'New Contact Us form is created by api',
        body,
        'testtestapp454545@gmail.com',
        ['ds_ch@i.ua'],
        fail_silently=False,
    )


@shared_task()
def print_hello_world_beat():
    print('BEAT')  # noqa
