from rest_framework import serializers
from currency.models import Rate, Bank, ContactUs


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = (
            'id',
            'name',
            # 'code_name',
            # 'url',
            'original_url',
            'number',
        )


class RateSerializer(serializers.ModelSerializer):
    # bank = BankSerializer(read_only=True)
    bank_object = BankSerializer(source='bank', read_only=True)

    class Meta:
        model = Rate
        fields = (
            'id',
            'type_curr',
            'buy',
            'sale',
            # 'created',
            'bank_object',
            'bank',
        )

        extra_kwargs = {
            'bank': {'write_only': True},
        }


class RateDetailsSerializer(serializers.ModelSerializer):

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


class BankDetailsSerializer(serializers.ModelSerializer):
    # rate_object = serializers.StringRelatedField(many=True)

    class Meta:
        model = Bank
        fields = (
            'id',
            'name',
            'code_name',
            'url',
            'original_url',
            'number',
            # 'rate_object',
        )


class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = (
            'id',
            'email_from',
            'subject',
            'message',
            # 'created',
        )


class ContactUsDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = (
            'id',
            'email_from',
            'subject',
            'message',
            'created',
        )
