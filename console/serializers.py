
from rest_framework import serializers
from .models import QRData, PhoneList, PhoneDetail


class QRDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRData
        fields = '__all__'


class PhoneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneList
        fields = '__all__'


class PhoneDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneDetail
        fields = '__all__'
