
from rest_framework import serializers
from .models import QRData, PhoneList, PhoneLocation


class QRDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRData
        fields = '__all__'


class PhoneListSerailizer(serializers.ModelSerializer):
    class Meta:
        model = PhoneList
        fields = '__all__'


class PhoneLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneLocation
        fields = '__all__'
