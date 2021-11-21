from django import forms

class Add_Wall_form(forms.Form):
    owner = forms.CharField(
        widget=forms.TextInput(),
        label='صاحب دیوار'
    )
    location = forms.CharField(
        widget=forms.TextInput(),
        label='آدرس'
    )
    start_date = forms.DateField(
        widget=forms.DateInput(),
        label='تاریخ شروع'
    )
    end_date = forms.DateField(
        widget=forms.DateInput(),
        label='تاریخ پایان'
    )
    space_count = forms.IntegerField(
        widget=forms.NumberInput(),
        label='تعداد گنجایش تصویر'
    )
    # image = forms.ImageField(
    #     label='تصویر دیوار'
    # )
    price = forms.IntegerField(
        widget=forms.NumberInput(),
        label='هزینه اجاره'
    )
