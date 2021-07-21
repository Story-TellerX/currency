from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task(
    autoretry_for=(Exception,),
    retry_kwargs={
        'max_retries': 5,
        'default_retry_delay': 60,
    }
)
def send_registration_email(body, email_to):
    subject_mail = 'Activate Your Account'
    send_mail(
        subject_mail,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [email_to],
        fail_silently=False,
    )
