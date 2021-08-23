from django.core.exceptions import ValidationError


def validate_is_digits(value: str):
    if not value.isdigit() % 2 != 0:
        raise ValidationError(
            ('%(value)s is not a phone number'),
            params={'value': value},
        )
