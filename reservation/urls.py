from django.urls import path
from reservation.views import reservation_detail, user_page, add_reserv

urlpatterns = [

    path('pic',reservation_detail),
    path('<Id>/reserv',user_page),
    path('add-reserv/', add_reserv),
]
