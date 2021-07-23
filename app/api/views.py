from rest_framework.response import Response

from currency.models import Rate, Bank
from api.serializers import RateSerializer, RateDetailsSerializer, BankSerializer, BankDetailsSerializer
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
    queryset = Rate.objects.all()
    # serializer_class = RateSerializer

    def get_serializer_class(self):
        if 'pk' in self.kwargs:
            return RateDetailsSerializer
        return RateSerializer


class BankViewSets(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    # serializer_class = BankSerializer

    def get_serializer_class(self):
        if 'pk' in self.kwargs:
            return BankDetailsSerializer
        return BankSerializer


class RateTypeChoicesView(APIView):
    def get(self, request, format=None):  # noqa
        # return a list of all users
        # usernames = [user.username in User.objects.all()]
        return Response(choices.RATE_TYPE_CHOICES)
