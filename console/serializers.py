
from rest_framework import serializers
from .models import *


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

# #

class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        fields = '__all__'


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'


class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class LuggageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Luggage
        fields = '__all__'


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


