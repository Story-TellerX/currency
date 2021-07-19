from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView

from currency.tasks import send_email_background
from currency.utils import generate_password
from currency.models import Rate, ContactUs, Bank
from currency.forms import RateForm, BankForm, ContactUsForm


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class GenPassword(TemplateView):
    template_name = 'gen_pass.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['number'] = generate_password()
        return context


class HelloWorld(TemplateView):
    template_name = 'hello.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['string'] = "Hello World from Class"
        return context


class RateListView(ListView):
    template_name = 'rate_list.html'
    queryset = Rate.objects.all().select_related('bank')


class RateCreateView(CreateView):
    model = Rate
    # fields = (
    #     'type_curr',
    #     'buy',
    #     'sale',
    #     'bank',
    # )
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_create.html'


class RateDetailView(LoginRequiredMixin, DetailView):
    template_name = 'rate_details.html'
    # model = Rate
    queryset = Rate.objects.all()


class RateUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'rate_update.html'
    queryset = Rate.objects.all()
    success_url = reverse_lazy('currency:rate-list')
    form_class = RateForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)


class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rate_confirm_delete.html'
    success_url = reverse_lazy('currency:rate-list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)


class BankListView(ListView):
    template_name = 'bank_list.html'
    queryset = Bank.objects.all()


class BankCreateView(CreateView):
    model = Bank
    # fields = (
    #     'name',
    #     'url',
    #     'number',
    # )
    form_class = BankForm
    success_url = reverse_lazy('currency:bank-list')
    template_name = 'bank_create.html'


class BankDetailView(DetailView):
    template_name = 'bank_details.html'
    # model = Bank
    queryset = Bank.objects.all()


class BankUpdateView(UpdateView):
    template_name = 'bank_update.html'
    queryset = Bank.objects.all()
    success_url = reverse_lazy('currency:bank-list')
    form_class = BankForm


class BankDeleteView(DeleteView):
    queryset = Bank.objects.all()
    template_name = 'bank_confirm_delete.html'
    success_url = reverse_lazy('currency:bank-list')


class ContactusListView(ListView):
    template_name = 'contactus_list.html'
    queryset = ContactUs.objects.all()


class CreateContactUs(CreateView):
    model = ContactUs
    # fields = (
    #     'email_from',
    #     'subject',
    #     'message',
    # )
    form_class = ContactUsForm
    success_url = reverse_lazy('currency:contactus-list')
    template_name = 'contactus_create.html'

    def form_valid(self, form):
        data = form.cleaned_data
        body = f'''
        From: {data['email_from']}
        Topic: {data['subject']}

        Message:
        {data['message']}
        '''
        # send_mail(
        #     'New Contact Us form is created',
        #     body,
        #     'testtestapp454545@gmail.com',
        #     ['ds_ch@i.ua'],
        #     fail_silently=False,
        # )
        send_email_background.delay(body)

        return super().form_valid(form)


class ContactusDetailView(DetailView):
    template_name = 'contactus_details.html'
    # model = ContactUS
    queryset = ContactUs.objects.all()
