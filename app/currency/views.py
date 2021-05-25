from django.http import HttpResponse
from currency.utils import generate_password


def gen_password(request):
    password = generate_password()
    return HttpResponse(password)


def hello_world(request):
    return HttpResponse('Hello World')
    # Added comment to display funcs
