from rest_framework.response import Response

from api.paginators import RatePagination, BankPagination
from currency.models import Rate, Bank, ContactUs
from api.serializers import (
    RateSerializer, RateDetailsSerializer, BankSerializer, ContactUsSerializer, ContactUsDetailsSerializer,

)  # BankDetailsSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView

from currency import choices


class RateList(generics.ListAPIView, generics.CreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class RateListCreate(generics.ListCreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class RateDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class RateViewSets(viewsets.ModelViewSet):
    queryset = Rate.objects.all().order_by('-created')
    # serializer_class = RateSerializer
    pagination_class = RatePagination

    def get_serializer_class(self):
        if 'pk' in self.kwargs:
            return RateDetailsSerializer
        return RateSerializer


class BankVListView(generics.ListAPIView):
    queryset = Bank.objects.all().order_by('id')
    serializer_class = BankSerializer
    pagination_class = BankPagination

    # def get_serializer_class(self):
    #     if 'pk' in self.kwargs:
    #         return BankDetailsSerializer
    #     return BankSerializer


class RateTypeChoicesView(APIView):
    def get(self, request, format=None):  # noqa
        # return a list of all users
        # usernames = [user.username in User.objects.all()]
        return Response(choices.RATE_TYPE_CHOICES)


class ContactUsViewSets(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all().order_by('id')
    pagination_class = RatePagination

    def get_serializer_class(self):
        if 'pk' in self.kwargs:
            return ContactUsDetailsSerializer
        return ContactUsSerializer
