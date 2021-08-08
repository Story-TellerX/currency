from django.core.management.base import BaseCommand
import datetime


class Command(BaseCommand):
    help = 'Parsing archive data of rates from PrivatBank API'  # noqa

    def handle(self, *args, **options):
        pass

    def get_date_for_parsing(self):
        current_date = str(datetime.date.today().strftime("%d.%m.%Y"))
        start = datetime.datetime.strptime("01.01.2015", "%d.%m.%Y")
        end = datetime.datetime.today().strptime(current_date, "%d.%m.%Y")
        date_generated_for_interval = []
        url_date_for_insert = []
        for x in range(0, (end - start).days):
            date_generated_for_interval.append(start + datetime.timedelta(days=x))
        for date in date_generated_for_interval:
            url_date_for_insert.append('https://api.privatbank.ua/p24api/exchange_rates?json&date=' + ''.join(date.strftime("%d.%m.%Y")))
        return url_date_for_insert

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


