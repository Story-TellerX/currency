# path('rate/list/', rate_list, name="rate-list"),
# path('contactus/create/', contactus_create, name="contactus-create"),

# from django.shortcuts import render, get_object_or_404, redirect  # reverse
# from django.http import HttpResponse  # HttpResponseRedirect, Http404
# from annoying.functions import get_object_or_None
# from django.shortcuts import render
# from django.http import HttpResponse


# def hello_world(request):
#     return HttpResponse('Hello World')
#     # Added comment to display funcs

# def gen_password(request):
#     password = generate_password()
#     return HttpResponse(password)

# def index(request):
#     return render(request, 'index.html')

# def rate_list(request):
#     queryset = Rate.objects.all()
#     # print(queryset.query)
#     # ids = []
#     # for rate in queryset:
#     #     ids.append(rate.id)
#
#     context = {
#         "objects": queryset,
#     }
#     return render(request, 'rate_list.html', context=context)
#
#
# def rate_details(request, pk):
#     # 127.0.0.1:8000/rate/details/?id=10
#     # 127.0.0.1:8000/rate/details/10/
#     # slug example Here Is My Title -> here-is-my-title
#
#     # id_ = request.GET['id']
#     # rate = Rate.objects.get(id=id_)
#
#     # try:
#     #     rate = Rate.objects.get(pk=pk)
#     # except Rate.DoesNotExist:
#     #     # rate = None
#     #     raise Http404(f"Rate does not exist with id={pk}")
#
#     rate = get_object_or_404(Rate, pk=pk)
#
#     context = {
#         'object': rate,
#     }
#     return render(request, 'rate_details.html', context=context)


# def rate_create(request):
#     # form_data = request.GET
#     # if form_data:
#     #     form = RateForm(form_data)
#     #     if form.is_valid():
#     #         form.save()
#     #         return HttpResponseRedirect('/currency/rate/list/')
#     # else:
#     #     form = RateForm()
#
#     if request.method == 'POST':
#         form_data = request.POST
#         form = RateForm(form_data)
#         if form.is_valid():
#             form.save()
#             # return HttpResponseRedirect('/currency/rate/list/')
#             # return HttpResponseRedirect(reverse('currency:rate-list'))
#             return redirect('currency:rate-list')
#     elif request.method == 'GET':
#         form = RateForm()
#
#     counter = Rate.objects.count()
#
#     context = {
#         # 'message': 'Rate create message',
#         'form': form,
#         'count': counter,
#     }
#     return render(request, "rate_create.html", context=context)
#
#
# def rate_update(request, pk):
#     instance = get_object_or_404(Rate, pk=pk)
#
#     if request.method == 'POST':
#         form_data = request.POST
#         form = RateForm(form_data, instance=instance)
#         if form.is_valid():
#             form.save()
#             # return HttpResponseRedirect('/currency/rate/list/')
#             return redirect('currency:rate-list')
#     elif request.method == 'GET':
#         form = RateForm(instance=instance)
#
#     context = {
#         'form': form,
#         'instance': instance,
#     }
#
#     return render(request, "rate_update.html", context=context)
#
#
# def rate_delete(request, pk):
#     instance = get_object_or_None(Rate, pk=pk)
#     # instance.delete()
#     if instance is not None:
#         instance.delete()
#     # return HttpResponseRedirect('/currency/rate/list/')
#     return redirect('currency:rate-list')

# def bank_list(request):
#     queryset = Bank.objects.all()
#
#     context = {
#         "objects": queryset,
#     }
#     return render(request, 'bank_list.html', context=context)

# def bank_details(request, pk):
#     banks = get_object_or_404(Bank, pk=pk)
#
#     context = {
#         'object': banks,
#     }
#     return render(request, 'bank_details.html', context=context)


# def bank_create(request):
#     if request.method == 'POST':
#         form_data = request.POST
#         form = BankForm(form_data)
#         if form.is_valid():
#             form.save()
#             # return HttpResponseRedirect('/currency/bank/list/')
#             return redirect('currency:bank-list')
#     elif request.method == 'GET':
#         form = BankForm()
#
#     counter = Bank.objects.count()
#
#     context = {
#         'form': form,
#         'count': counter,
#     }
#     return render(request, "bank_create.html", context=context)

# def bank_update(request, pk):
#     instance = get_object_or_404(Bank, pk=pk)
#     if request.method == 'POST':
#         form_data = request.POST
#         form = BankForm(form_data, instance=instance)
#         if form.is_valid():
#             form.save()
#             # return HttpResponseRedirect('/currency/bank/list/')
#             return redirect('currency:bank-list')
#     elif request.method == 'GET':
#         form = BankForm(instance=instance)
#
#     context = {
#         'form': form,
#         'instance': instance,
#     }
#     return render(request, "bank_update.html", context=context)

# def bank_delete(request, pk):
#     instance = get_object_or_None(Bank, pk=pk)
#     if instance is not None:
#         instance.delete()
#     # return HttpResponseRedirect('/currency/bank/list/')
#     return redirect('currency:bank-list')

# def contactus_list(request):
#     queryset = ContactUs.objects.all()
#
#     context = {
#         "objects": queryset,
#     }
#     return render(request, 'contactus_list.html', context=context)

# def contactus_details(request, pk):
#     contactus = get_object_or_404(ContactUs, pk=pk)
#
#     context = {
#         'object': contactus,
#     }
#     return render(request, 'contactus_details.html', context=context)

# def contactus_create(request):
#     if request.method == 'POST':
#         form_data = request.POST
#         form = ContactusForm(form_data)
#         if form.is_valid():
#             form.save()
#             # return HttpResponseRedirect('/currency/contactus/list/')
#             return redirect('currency:contactus-list')
#     elif request.method == 'GET':
#         form = ContactusForm()
#
#     counter = ContactUs.objects.count()
#
#     context = {
#         'form': form,
#         'count': counter,
#     }
#     return render(request, "contactus_create.html", context=context)
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

# TODO create custom command to override codename
# b = Bank.objects.get(name='MonoBank')
# b.code_name
# b.code_name = 'monobank'
# b.save()
# b = Bank.objects.get(name='Vkurse')
# b.code_name
# b.code_name = 'vkurse'
# b.save()
# b = Bank.objects.get(name='IBoxBank')
# b.code_name
# b.code_name = 'iboxbank'
# b.save()
# b = Bank.objects.get(name='GrantBank')
# b.code_name
# b.code_name = 'grantbank'
# b.save()
# b = Bank.objects.get(name='SkyBank')
# b.code_name
# b.code_name = 'skybank'
# b.save()

# CACHE EXAMPLEs
from time import sleep
CACHE = {}
# CACHE = {
#     'slow_func': {},
#     'slow_func2': {},
# }
# CACHE2 = {}


def slow_func(sleep_time, mult=1):

    cache_key = f'slow_func_{sleep_time}_{mult}'

    # if sleep_time in CACHE:
    #     return CACHE[sleep_time]

    if cache_key in CACHE:
        return CACHE[cache_key]

    sleep(sleep_time)
    result = sleep_time * 2 * mult
    CACHE[cache_key] = result
    return result

# def slow_func2(sleep_time):
#
#     cache_key = f'slow_func2_{sleep_time}'
#
#     # if sleep_time incache_key CACHE2:
#     #     return CACHE2[sleep_time]
#     # if sleep_time in CACHE:
#     #     return CACHE[sleep_time]
#     if cache_key in CACHE:
#         return CACHE[cache_key]
#
#     sleep(sleep_time)
#     result = sleep_time * 3
#     # CACHE2[sleep_time] = result
#     CACHE[cache_key] = result
#     return result

# print(slow_func(3, 2))
# print(slow_func(4, 3))
# print(slow_func(3, 3))
# print(slow_func(4, 3))
# print(slow_func2(3))
# print(slow_func2(3))
# print(slow_func2(4))
# print(slow_func2(4))
# print(CACHE)
