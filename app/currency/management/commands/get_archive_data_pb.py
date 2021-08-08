import time

import requests
from django.core.management.base import BaseCommand
import datetime

from currency import consts, choices
from currency.utils import to_decimal


class Command(BaseCommand):
    help = 'Parsing archive data of rates from PrivatBank API'  # noqa

    def get_date_for_parsing(self):
        current_date = str(datetime.date.today().strftime('%d.%m.%Y'))
        start = datetime.datetime.strptime('01.01.2015', '%d.%m.%Y')
        end = datetime.datetime.today().strptime(current_date, '%d.%m.%Y')
        date_generated_for_interval = []
        url_date_for_insert = []
        for x in range(0, (end - start).days):
            date_generated_for_interval.append(start + datetime.timedelta(days=x))
        for date in date_generated_for_interval:
            url_date_for_insert.append('https://api.privatbank.ua/p24api/'
                                       'exchange_rates?json&date=' + ''.join(date.strftime('%d.%m.%Y')))
        return url_date_for_insert

    def get_privat_archive_currencies(self, url_date_for_insert):
        response = requests.get(url_date_for_insert)
        response.raise_for_status()
        currencies = response.json()
        return currencies

    def parse_privatbank_archive(self, url):
        from currency.models import Rate, Bank

        currencies = self.get_privat_archive_currencies(url)

        bank = Bank.objects.get(code_name=consts.CODE_NAME_PRIVATBANK)

        available_currencies_types = {
            'USD': choices.RATE_TYPE_USD,
            'EUR': choices.RATE_TYPE_EUR,
        }

        currencies_data = currencies['exchangeRate']

        for curr in currencies_data:
            currencies_type = curr['currency']
            if currencies_type in available_currencies_types:
                currencies_type = available_currencies_types[curr['currency']]
                buy = to_decimal(curr['purchaseRate'])
                sale = to_decimal(curr['saleRate'])
                rate_date_string = currencies['date']
                rate_date = datetime.datetime.strptime(rate_date_string, '%d.%m.%Y').date()

                previous_rate = Rate.objects.filter(bank=bank, type_curr=currencies_type).order_by('rate_dates').last()

                if previous_rate is None or \
                        previous_rate.sale != sale or \
                        previous_rate.buy != buy or \
                        previous_rate.rate_dates != rate_date:
                    Rate.objects.create(
                        type_curr=currencies_type,
                        sale=sale,
                        buy=buy,
                        bank=bank,
                        rate_dates=rate_date,
                    )

    def handle(self, *args, **options):
        from currency.models import Rate, Bank
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        bank = Bank.objects.get(code_name=consts.CODE_NAME_PRIVATBANK)
        rate_dates_in_db = Rate.objects.filter(bank=bank).order_by('rate_dates').last()
        url_date_for_insert = self.get_date_for_parsing()
        while rate_dates_in_db.rate_dates != yesterday:
            for url in url_date_for_insert:
                self.parse_privatbank_archive(url)
                time.sleep(10)

        # FIRST TRY TO GET INTERVAL OF DATES
        # initial_date = ('201412')
        # year = int(initial_date[:-2])  # parse year
        # month = int(initial_date[4:])  # parse month
        # num_days = calendar.monthrange(
        #     int(initial_date[:-2]),
        #     int(initial_date[4:])
        # )[1]  # get numbers of days in month
        # list_of_dates_per_month_year = []
        # for day in range(1, num_days + 1):
        #     list_of_dates_per_month_year.append(
        #         datetime.date(year, month, day).strftime('%d.%m.%Y')  # get date for month in year with days
        #         #  formating output for url in parser
        #     )
