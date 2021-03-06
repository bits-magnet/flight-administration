from django.shortcuts import render
from rest_framework import generics


def index(request):
    return render(request, 'index.html')


def map(request):
    return render(request, 'map.html')

# #


from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class CitizenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer


class CitizenList(generics.ListCreateAPIView):
    serializer_class = CitizenSerializer
    queryset = Citizen.objects.all()
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter,)
    filter_fields = '__all__'
    ordering_fields = '__all__'
    # search_fields = ('facilities',)


class AirportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airports.objects.all()
    serializer_class = AirportSerializer


class AirportList(generics.ListCreateAPIView):
    serializer_class = AirportSerializer
    queryset = Airports.objects.all()
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter,)
    filter_fields = '__all__'
    ordering_fields = '__all__'


class PlaneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer


class PlaneList(generics.ListCreateAPIView):
    serializer_class = PlaneSerializer
    queryset = Plane.objects.all()
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter,)
    filter_fields = '__all__'
    ordering_fields = '__all__'


class FlightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class FlightList(generics.ListCreateAPIView):
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter,)
    filter_fields = '__all__'
    ordering_fields = '__all__'


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingList(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter,)
    filter_fields = '__all__'
    ordering_fields = '__all__'


class LuggageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Luggage.objects.all()
    serializer_class = LuggageSerializer


class LuggageList(generics.ListCreateAPIView):
    serializer_class = LuggageSerializer
    queryset = Luggage.objects.all()
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter,)
    filter_fields = '__all__'
    ordering_fields = '__all__'


class PromotionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer


class PromotionList(generics.ListCreateAPIView):
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.all()
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter,)
    filter_fields = '__all__'
    ordering_fields = '__all__'


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionList(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter,)
    filter_fields = '__all__'
    ordering_fields = '__all__'



