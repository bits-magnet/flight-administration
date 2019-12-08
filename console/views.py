from django.shortcuts import render
from .models import PhoneList, QRData, PhoneDetail
from rest_framework import generics
from .serializers import PhoneListSerializer, QRDataSerializer, PhoneDetailSerializer


def index(request):
    return render(request, 'index.html')


def map(request):
    return render(request, 'map.html')


def see_map_by_id(request, pk):
    device = PhoneDetail.objects.get(id=pk)
    print(device)
    context = {
        'device' : device
    }
    return render(request, 'map.html', context)


def devices(request):
    devices = PhoneDetail.objects.all()
    context = {
        'devices': devices
    }
    print(devices)
    return render(request, 'devicelist.html', context)


class PhoneListView(generics.ListCreateAPIView):
    serializer_class = PhoneListSerializer
    queryset = PhoneList.objects.all()
    filter_fields = '__all__'
    ordering_fields = '__all__'


class PhoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhoneList.objects.all()
    serializer_class = PhoneListSerializer


class QRDataListView(generics.ListCreateAPIView):
    serializer_class = QRDataSerializer
    queryset = QRData.objects.all()
    filter_fields = '__all__'
    ordering_fields = '__all__'


class QRDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QRData.objects.all()
    serializer_class = QRDataSerializer


class PhoneLoactionListView(generics.ListCreateAPIView):
    serializer_class = PhoneDetailSerializer
    queryset = PhoneDetail.objects.all()
    filter_fields = '__all__'
    ordering_fields = '__all__'


class QRDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhoneDetail.objects.all()
    serializer_class = PhoneDetailSerializer


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
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AirportList(generics.ListCreateAPIView):
    serializer_class = AirportSerializer
    queryset = Airport.objects.all()
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



