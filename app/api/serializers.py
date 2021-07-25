from rest_framework import serializers
from currency.models import Rate, Bank, ContactUs


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = (
            'id',
            'type_curr',
            'buy',
            'sale',
            # 'created',
            'bank_id',
        )


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


# class BankDetailsSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Bank
#         fields = (
#             'id',
#             'name',
#             'code_name',
#             'url',
#             'original_url',
#             'number',
#         )

class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = (
            'id',
            'email_from',
            'subject',
            # 'message',
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
