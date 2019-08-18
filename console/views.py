from django.shortcuts import render
from .models import PhoneList, QRData, PhoneDetail
from rest_framework import generics
from .serializers import PhoneListSerializer, QRDataSerializer, PhoneDetailSerializer


def map(request):
    return render(request, 'map.html')


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
