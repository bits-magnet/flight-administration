from django.contrib import admin
from .models import PhoneList, QRData, PhoneDetail


admin.site.register(QRData)
admin.site.register(PhoneList)
admin.site.register(PhoneDetail)

