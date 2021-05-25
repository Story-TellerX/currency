import string
import random


def generate_password(length: int = 10) -> str:
    chars = string.ascii_letters + string.digits
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return str(password)
