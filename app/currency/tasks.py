from celery import shared_task
from django.core.mail import send_mail


# @shared_task
# def print_hello_world():
#     from time import sleep
#     sleep(10)
#     print('Hello world from celery process')


# @shared_task
# def print_hello_world(num):
#     from time import sleep
#     sleep(num)
#     print(f'Hello world from celery process wait {num}')


# @shared_task
# def print_hello_world(rate_id):
#     from currency.models import Rate
#     rate = Rate.objects.get(id=rate_id)
#     print(f'Got Rate with id: {rate.id}')


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
