from django.db import models
from django.contrib.auth.models import AbstractUser


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'uploads/avatars/{0}/{1}'.format(instance.id, filename)


class User(AbstractUser):
    avatar = models.FileField(null=True, blank=True, default=None, upload_to=user_directory_path)
    # upload_to='uploads/%Y/%m/%d/' can be used
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    email = models.EmailField(
        'email address',
        blank=False,
        null=False,
        unique=True,
    )
