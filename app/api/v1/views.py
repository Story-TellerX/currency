from rest_framework.response import Response

from api.v1.filters import RateFilter, ContactUsFilter
from api.v1.paginators import RatePagination, BankPagination
from currency.models import Rate, Bank, ContactUs
from api.v1.serializers import (
    RateSerializer, RateDetailsSerializer, BankSerializer, ContactUsSerializer, ContactUsDetailsSerializer,
    BankDetailsSerializer,

)
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.views import APIView
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters
from currency import choices
from currency.tasks import send_email_from_api_background


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
    queryset = Rate.objects.all().select_related('bank').order_by('-created')
    # serializer_class = RateSerializer
    pagination_class = RatePagination

    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
        rest_framework_filters.SearchFilter,
    )
    filterset_class = RateFilter

    ordering_fields = ['id', 'created', 'type_curr', "sale", 'buy']

    search_fields = ['sale', 'buy', '=id', 'created', 'type_curr']

    def get_serializer_class(self):
        if 'pk' in self.kwargs:
            return RateDetailsSerializer
        return RateSerializer


# class BankVListView(generics.ListAPIView):
# I will try to get reverse foreign key
# before it was used listAPI
class BankVListView(viewsets.ModelViewSet):
    queryset = Bank.objects.all().order_by('id')
    serializer_class = BankSerializer
    pagination_class = BankPagination

    def get_serializer_class(self):
        if 'pk' in self.kwargs:
            return BankDetailsSerializer
        return BankSerializer


class RateTypeChoicesView(APIView):
    def get(self, request, format=None):  # noqa
        # return a list of all users
        # usernames = [user.username in User.objects.all()]
        return Response(choices.RATE_TYPE_CHOICES)


class ContactUsViewSets(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all().order_by('id')
    pagination_class = RatePagination

    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
        rest_framework_filters.SearchFilter,
    )
    filterset_class = ContactUsFilter

    ordering_fields = ['id', 'created', 'email_from', 'subject', 'message']

    search_fields = ['=id', 'created', 'email_from', '^subject', 'message']

    def get_serializer_class(self):
        if 'pk' in self.kwargs:
            return ContactUsDetailsSerializer
        return ContactUsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = serializer.data
        body = f'''
        From: {data['email_from']}
        Topic: {data['subject']}

        Message:
        {data['message']}
        '''
        send_email_from_api_background.delay(body)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
