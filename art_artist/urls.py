from django.urls import path
from art_artist.views import add_art

urlpatterns = [

    path('add-art',add_art),
]