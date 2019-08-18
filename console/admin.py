from django.contrib import admin
from .models import PhoneList, QRData, PhoneLocation


admin.site.register(QRData)
admin.site.register(PhoneList)
admin.site.register(PhoneLocation)