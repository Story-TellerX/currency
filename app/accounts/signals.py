from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver

from accounts.models import User


@receiver(pre_save, sender=User)
def pre_save_profile_phone(sender, instance, **kwargs):
    instance.phone = ''.join(char for char in instance.phone if char.isdigit())
    # instance.profile.save()
    # print('PRE SAVE WORKS')


@receiver(pre_save, sender=User)
def pre_save_profile_email(sender, instance, **kwargs):
    if instance.email:
        instance.email = str(instance.email).lower()


@receiver(post_save, sender=User)
def post_save_user_send_to_cool_service(sender, instance, created, **kwargs):
    # print(f'Instance is created: {created}. Instance: {instance}')
    if created:
        print('Send to some cool service)')  # noqa
        # print('Send to some awesome service)'  # Bad practice - better create a separate signal


@receiver(post_save, sender=User)
def post_save_user_send_to_awesome_service(sender, instance, created, **kwargs):
    # print(f'Instance is created: {created}. Instance: {instance}')
    if created:
        print('Send to some awesome service))')  # noqa


class DeleteDenied(Exception):
    pass


@receiver(pre_delete, sender=User)
def user_deleting_is_denied(sender, *args, **kwargs):
    raise DeleteDenied('Deleting user is not allowed')
