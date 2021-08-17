from django.db import models
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static

# from accounts.validators import validate_is_digits


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
    phone = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        default=None,
        # validators=(validate_is_digits, )
    )

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return static('images/default-user.jpg')

    def save(self, *args, **kwargs):
        # print('Before save')
        if self.pk:  # if object was created
            pass
        if self.phone:
            self.phone = ''.join(char for char in self.phone if char.isdigit())
        super().save(*args, **kwargs)
        # print('After save')
