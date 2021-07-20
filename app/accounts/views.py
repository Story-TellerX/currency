from annoying.functions import get_object_or_None
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, RedirectView

from accounts.forms import SignUpForm
from accounts.models import User


class MyProfile(LoginRequiredMixin, UpdateView):
    template_name = 'my-profile.html'
    queryset = User.objects.all()
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name',
    )

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filters(pk=self.request.user.pk)
    #     return queryset

    def get_object(self, queryset=None):
        return self.request.user


class SignUp(CreateView):
    model = User
    template_name = 'signup.html'
    success_url = reverse_lazy('index')
    form_class = SignUpForm


class ActivateAccount(RedirectView):
    pattern_name = 'index'

    """
    messages.debug(request, '%s SQL statements were executed.' % count)
    messages.success(request, 'Profile details updated.')
    messages.error(request, 'Document deleted.')
    """

    def get_redirect_url(self, *args, **kwargs):
        activation_key = kwargs.pop('activation_key')
        user = get_object_or_None(User, username=activation_key)
        if user:
            if user.is_active:
                messages.warning(self.request, 'Your account is already activated.')
            else:
                messages.info(self.request, 'Thanks for activating your account.')
                user.is_active = True
                user.save()
        response = super().get_redirect_url(*args, **kwargs)
        return response
