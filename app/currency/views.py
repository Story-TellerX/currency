from annoying.functions import get_object_or_None
from django.http import HttpResponse, HttpResponseRedirect  # Http404
from django.shortcuts import render, get_object_or_404

from currency.utils import generate_password
from currency.models import Rate, ContactUs, Bank
from currency.forms import RateForm, BankForm, ContactusForm


def gen_password(request):
    password = generate_password()
    return HttpResponse(password)


def hello_world(request):
    return HttpResponse('Hello World')
    # Added comment to display funcs


def rate_list(request):
    queryset = Rate.objects.all()
    # print(queryset.query)
    # ids = []
    # for rate in queryset:
    #     ids.append(rate.id)

    context = {
        "objects": queryset,
    }

    return render(request, 'rate_list.html', context=context)


def rate_details(request, pk):
    # 127.0.0.1:8000/rate/details/?id=10
    # 127.0.0.1:8000/rate/details/10/
    # slug example Here Is My Title -> here-is-my-title

    # id_ = request.GET['id']
    # rate = Rate.objects.get(id=id_)

    # try:
    #     rate = Rate.objects.get(pk=pk)
    # except Rate.DoesNotExist:
    #     # rate = None
    #     raise Http404(f"Rate does not exist with id={pk}")

    rate = get_object_or_404(Rate, pk=pk)

    context = {
        'object': rate,
    }
    return render(request, 'rate_details.html', context=context)


def contactus_list(request):
    queryset = ContactUs.objects.all()

    context = {
        "objects": queryset,
    }

    return render(request, 'contactus_list.html', context=context)


def contactus_details(request, pk):

    contactus = get_object_or_404(ContactUs, pk=pk)

    context = {
        'object': contactus,
    }
    return render(request, 'contactus_details.html', context=context)


def bank_list(request):
    queryset = Bank.objects.all()

    context = {
        "objects": queryset,
    }

    return render(request, 'bank_list.html', context=context)


def bank_details(request, pk):

    banks = get_object_or_404(Bank, pk=pk)

    context = {
        'object': banks,
    }

    return render(request, 'bank_details.html', context=context)


def rate_create(request):
    # form_data = request.GET
    # if form_data:
    #     form = RateForm(form_data)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/currency/rate/list/')
    # else:
    #     form = RateForm()

    if request.method == 'POST':
        form_data = request.POST
        form = RateForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/rate/list/')
    elif request.method == 'GET':
        form = RateForm()

    counter = Rate.objects.count()

    context = {
        # 'message': 'Rate create message',
        'form': form,
        'count': counter,
    }
    return render(request, "rate_create.html", context=context)


def rate_update(request, pk):
    instance = get_object_or_404(Rate, pk=pk)

    if request.method == 'POST':
        form_data = request.POST
        form = RateForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/rate/list/')
    elif request.method == 'GET':
        form = RateForm(instance=instance)

    context = {
        'form': form,
        'instance': instance,
    }

    return render(request, "rate_update.html", context=context)


def rate_delete(request, pk):
    instance = get_object_or_None(Rate, pk=pk)
    # instance.delete()
    if instance is not None:
        instance.delete()
    return HttpResponseRedirect('/currency/rate/list/')


def bank_create(request):
    if request.method == 'POST':
        form_data = request.POST
        form = BankForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/bank/list/')
    elif request.method == 'GET':
        form = BankForm()

    counter = Bank.objects.count()

    context = {
        'form': form,
        'count': counter,
    }
    return render(request, "bank_create.html", context=context)


def bank_update(request, pk):
    instance = get_object_or_404(Bank, pk=pk)
    if request.method == 'POST':
        form_data = request.POST
        form = BankForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/bank/list/')
    elif request.method == 'GET':
        form = BankForm(instance=instance)

    context = {
        'form': form,
        'instance': instance,
    }
    return render(request, "bank_update.html", context=context)


def bank_delete(request, pk):
    instance = get_object_or_None(Bank, pk=pk)
    if instance is not None:
        instance.delete()
    return HttpResponseRedirect('/currency/bank/list/')


def contactus_create(request):
    if request.method == 'POST':
        form_data = request.POST
        form = ContactusForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/contactus/list/')
    elif request.method == 'GET':
        form = ContactusForm()

    counter = ContactUs.objects.count()

    context = {
        'form': form,
        'count': counter,
    }
    return render(request, "contactus_create.html", context=context)
