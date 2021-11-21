from django.contrib import admin
from .models import Reserv

class ReservAdmin(admin.ModelAdmin):
    list_display = ['title','subject','active']
    list_filter = ['active']
    list_editable = ['active']
    search_fields = ['subject']

    class Meta:
        model = Reserv

admin.site.register(Reserv,ReservAdmin)