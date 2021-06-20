from django import forms

from currency.models import Rate, Bank


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'type_curr',
            'buy',
            'sale',
            'source',
        )


class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = (
            'name',
            'url',
            'number',
        )
