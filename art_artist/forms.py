from django import forms
from PIL import Image
from django.core import validators

class ArtForm(forms.Form):

    title = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder':'نام'}),
        label = 'نام',
        validators=[
            validators.MaxLengthValidator(150, 'نام و نام خانوادگی شما نمیتواند بیشتر از 150 کاراکتر باشد')
        ]
    )

    paintistname = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام نقاش'}),
        label='نام نقاش',
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'موضوع'}),
        label='موضوع',
    )

    about = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'توضیحات'}),
        label='توضیحات',
    )

    date = forms.DateField(
        widget=forms.DateInput(attrs={'placeholder': 'تاریخ ایجاد'}),
        label='تاریخ ایجاد',
    )

    material = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'متریال'}),
        label='متریال',
    )

    image = forms.ImageField(
        label='تصویر',
    )

