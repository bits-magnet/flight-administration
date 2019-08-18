from django.conf.urls import url
from .views import QRDataListView, QRDataDetailView, PhoneListView, PhoneDetailView, map, devices, see_map_by_id
from django.urls import path

urlpatterns = [
    path('api/phone/', PhoneListView.as_view()),
    path('api/phone/<int:pk>', PhoneDetailView.as_view()),
    path('api/qr/', QRDataListView.as_view()),
    path('api/qr/<int:pk>', QRDataDetailView.as_view()),
    path('map/', map),
    path('devices/', devices),
    path('devices/<int:pk>/map/', see_map_by_id),
]
