from django.contrib import admin
from .models import *


admin.site.register(QRData)
admin.site.register(PhoneList)
admin.site.register(PhoneDetail)

# #

admin.site.register(Citizen)
admin.site.register(Airport)
admin.site.register(Plane)
admin.site.register(Flight)
admin.site.register(Booking)
admin.site.register(Luggage)
admin.site.register(Promotion)
admin.site.register(Transaction)
