from django.db import models


class Rate(models.Model):
    type_curr = models.CharField(max_length=5)
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=64)

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


class Bank(models.Model):
    name = models.CharField(max_length=60)
    url = models.URLField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    number = models.CharField(max_length=30)

    def __str__(self):
        return f'Bank id: {self.id}'
