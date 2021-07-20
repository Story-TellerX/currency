from django.db import models
from django.db.models import PositiveSmallIntegerField
from currency import choices


class Bank(models.Model):
    name = models.CharField(max_length=64)
    code_name = models.CharField(
        max_length=64)
    url = models.URLField()
    original_url = models.URLField()
    number = models.CharField(max_length=30)

    def __str__(self):
        return f'Bank id: {self.id}'


class Rate(models.Model):
    # get_{field_name}_display()
    type_curr = PositiveSmallIntegerField(choices=choices.RATE_TYPE_CHOICES)
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    bank = models.ForeignKey(
        Bank,
        on_delete=models.CASCADE,
        null=True,
        default=None,
    )

    # bank = models.ForeignKey('currency.Bank')

    def __str__(self):
        return f'Rate id: {self.id}'


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=50)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=2500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'ContactUs id: {self.id}'

    # def save(self, *args, **kwargs):
    #     return super().save(*args, **kwargs)


class AnalyticsLog(models.Model):
    path = models.CharField(max_length=255)
    counter = models.PositiveBigIntegerField()
    request_method = PositiveSmallIntegerField(choices=choices.REQUEST_METHOD_CHOICES)
    status_code = models.CharField(max_length=3)

    # class Meta:
    #     # unique_together = [
    #     #     # ['path', 'request_method'],
    #     #     ['path', 'status_code'],
    #     # ]
