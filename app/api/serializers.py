from rest_framework import serializers
from currency.models import Rate, Bank


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = (
            'id',
            'type_curr',
            'buy',
            'sale',
            'created',
            'bank_id',
        )


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = (
            'id',
            'name',
            'code_name',
            'url',
            'original_url',
            'number',
        )
