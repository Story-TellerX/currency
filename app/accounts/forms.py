import uuid
from django import forms
from accounts.models import User


class SignUpForm(forms.ModelForm):

    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = (
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        instance = super().save(commit=False)

        # instance.username = 'HELLO'
        # instance.username = self.cleaned_data['email']
        instance.username = str(uuid.uuid4())
        instance.is_active = False

        if commit:
            instance.save()

        return instance
