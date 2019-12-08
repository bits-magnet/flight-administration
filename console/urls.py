from django.conf.urls import url
from .views import *
from django.urls import path

urlpatterns = [
    path('api/phone/', PhoneListView.as_view()),
    path('api/phone/<int:pk>', PhoneDetailView.as_view()),
    path('api/qr/', QRDataListView.as_view()),
    path('api/qr/<int:pk>', QRDataDetailView.as_view()),
    path('map/', map),
    path('devices/', devices),
    path('devices/<int:pk>/map/', see_map_by_id),
    path('', index),
    path('api/citizen/', CitizenList.as_view()),
    path('api/citizen/<int:pk>', CitizenDetail.as_view()),
    path('api/airport/', AirportList.as_view()),
    path('api/airport/<int:pk>', AirportDetail.as_view()),
    path('api/plane/', PlaneList.as_view()),
    path('api/plane/<int:pk>', PlaneDetail.as_view()),
    path('api/flight/', FlightList.as_view()),
    path('api/flight/<int:pk>', FlightDetail.as_view()),
    path('api/booking/', BookingList.as_view()),
    path('api/booking/<int:pk>', BookingDetail.as_view()),
    path('api/promotion/', PromotionList.as_view()),
    path('api/promotion/<int:pk>', PromotionDetail.as_view()),
    path('api/transaction/', TransactionList.as_view()),
    path('api/transaction/<int:pk>', TransactionDetail.as_view()),
]
