from rest_framework import serializers
from currency.models import Rate


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
