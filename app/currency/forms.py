from django import forms

from currency.models import Rate, Bank, ContactUs


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'type_curr',
            'buy',
            'sale',
            'bank',
        )


class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = (
            'name',
            'code_name',
            'url',
            'original_url',
            'number',
            'bank_logo',
        )


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'email_from',
            'subject',
            'message',
        )

    # def save(self, commit=True):
    #     return super().save(commit)
