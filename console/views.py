from django.shortcuts import render
from .models import PhoneList, QRData
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend,OrderingFilter
from .serializers import PhoneListSerailizer, QRDataSerializer


class PhoneListView(generics.ListCreateAPIView):
    serializer_class = PhoneListSerailizer
    queryset = PhoneList.objects.all()
    filter_fields = '__all__'
    ordering_fields = '__all__'


class PhoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhoneList.objects.all()
    serializer_class = PhoneListSerailizer


class QRDataListView(generics.ListCreateAPIView):
    serializer_class = QRDataSerializer
    queryset = QRData.objects.all()
    filter_fields = '__all__'
    ordering_fields = '__all__'


class QRDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QRData.objects.all()
    serializer_class = QRDataSerializer

