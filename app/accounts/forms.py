from django import forms
from accounts.models import User


class SignUpForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'email',
        )
