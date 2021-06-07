from django.core.management.base import BaseCommand
from currency.models import Bank
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Generate random records for Rate table'  # noqa

    def handle(self, *args, **options):
        fake = Faker()
        for index in range(100):
            Bank.objects.create(
                name=random.choice(('monobank', 'privatbank', 'vkurse', 'oshadbank', 'otp', 'pumb')),
                url=fake.url(),
                number=fake.phone_number(),
            )
