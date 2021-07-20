from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
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
