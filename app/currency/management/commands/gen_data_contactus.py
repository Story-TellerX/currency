from django.core.management.base import BaseCommand
from currency.models import ContactUs
from faker import Faker


class Command(BaseCommand):
    help = 'Generate random records for contact us table'  # noqa

    def handle(self, *args, **options):
        faker = Faker()
        for index in range(100):
            ContactUs.objects.create(
                email_from=faker.unique.email(),
                subject=faker.unique.sentence(nb_words=10, variable_nb_words=False),
                message=faker.text(max_nb_chars=500),
            )
