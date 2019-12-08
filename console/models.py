from django.db import models
from django.utils import timezone

# # #

class Airports(models.Model):
    name = models.CharField(default='', max_length=50)
    code = models.CharField(default='', max_length=10)
    latitude = models.IntegerField()
    longitude = models.IntegerField()



class Citizen(models.Model):
    name = models.CharField(default='', max_length=50)
    age = models.IntegerField()
    passport_number = models.IntegerField()

class Plane(models.Model):
    company = models.CharField(default='', max_length=50)
    plane_id = models.IntegerField()


class Flight(models.Model):
    flight_from = models.ForeignKey(Airports, related_name='flight_from', on_delete=models.CASCADE)
    flight_to = models.ForeignKey(Airports, related_name='flight_to', on_delete=models.CASCADE)
    plane_id = models.ForeignKey(Plane, on_delete=models.CASCADE)
    time_of_arrival = models.DateTimeField(default=timezone.now)
    time_of_boarding = models.DateTimeField(default=timezone.now)
    stay_time = models.DurationField()
    cost = models.IntegerField()
    business_capacity = models.IntegerField()
    economy_capacity = models.IntegerField()
    buisness_vacant = models.IntegerField()
    economy_vacant = models.IntegerField()


class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    STATES = [(0, 'NA'), (1, 'FINISHED'), (2, 'INTRANSIT'), (3, 'CANCELLED'), (4, 'FUTURE')]
    state = models.IntegerField(choices=STATES, default=0)


class Luggage(models.Model):
    weight = models.IntegerField()
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)


class Promotion(models.Model):
    name = models.CharField(default='', max_length=50)
    discount_code = models.IntegerField()
    discount_percent = models.IntegerField()
    valid = models.BooleanField(default=False)


class Transaction(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
