from django import forms
from art_artist.models import Art
from reservation.models import Reserv
from wall.models import Wall
from django.forms import ModelForm


class ArticleForm(ModelForm):
    class Meta:
        model = Reserv
        fields = ['title', 'subject', 'start_date', 'end_date','about','price','art','wall']
