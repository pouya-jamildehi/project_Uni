from django.contrib import admin
from.models import Art
# Register your models here.
class Art_Admin(admin.ModelAdmin):
    list_display = ['__str__','title','paintistname','active']

    class Meta:
        model = Art

admin.site.register(Art,Art_Admin)