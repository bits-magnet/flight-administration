from django.db import models


class PhoneList(models.Model):
    name = models.CharField(max_length=100, default='')
    number = models.IntegerField()

    def __str__(self):
        return self.name


class QRData(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField()
    number = models.IntegerField()
    building = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class PhoneDetail(models.Model):
    device_id = models.CharField(default='', max_length=100)
    device_name = models.CharField(default='', max_length=100)
    center_lat = models.FloatField(default=0)
    center_lon = models.FloatField(default=0)
    device_lat = models.FloatField(default=0)
    device_lon = models.FloatField(default=0)
    inrange = models.BooleanField(default=False)

    def __str__(self):
        return str(self.device_lat) + ' ' + str(self.device_lon)
