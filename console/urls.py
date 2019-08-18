from django.conf.urls import url
from .views import QRDataListView, QRDataDetailView, PhoneListView, PhoneDetailView
from django.urls import path

urlpatterns = [
    path('api/phone/', PhoneListView.as_view()),
    path('api/phone/<int:pk>', PhoneDetailView.as_view()),
    path('api/qr/', QRDataListView.as_view()),
    path('api/qr/<int:pk>', QRDataDetailView.as_view()),
]
