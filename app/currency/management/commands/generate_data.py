from django.core.management.base import BaseCommand
from currency.models import Rate
import random


class Command(BaseCommand):
    help = 'Generate random records for Rate table'  # noqa

    def handle(self, *args, **options):
        for index in range(100):
            Rate.objects.create(
                type_curr=random.choice(('usd', 'eur')),  # Faker lib can be used by faker.currency_code() with locale
                sale=random.uniform(20.00, 29.99),
                buy=random.uniform(20.00, 29.99),
                source=random.choice(('monobank', 'privatbank', 'vkurse')),
            )
