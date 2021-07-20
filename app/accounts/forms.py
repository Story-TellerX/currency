import uuid
from django import forms
from accounts.models import User
from accounts.tasks import send_registration_email
from django.conf import settings


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

    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password1'] != cleaned_data['password2']:
                # self.add_error('password', 'Password do not match')
                raise forms.ValidationError('Password do not match')
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        # instance.username = 'HELLO'
        # instance.username = self.cleaned_data['email']
        instance.username = str(uuid.uuid4())
        instance.is_active = False

        if commit:
            instance.save()

        body = f'''
        Activate Your Account
        {settings.DOMAIN}/activate/uuid
        '''

        send_registration_email.delay(body, self.cleaned_data['email'])
        # email address can be taken from  instance.email

        return instance
