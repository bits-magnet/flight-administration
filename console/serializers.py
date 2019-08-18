
from rest_framework import serializers
from .models import QRData, PhoneList


class QRDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRData
        fields = '__all__'


class PhoneListSerailizer(serializers.ModelSerializer):
    class Meta:
        model = PhoneList
        fields = '__all__'

