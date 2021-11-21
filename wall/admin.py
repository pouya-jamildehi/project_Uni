from django.contrib import admin
from .models import Wall
# Register your models here.
class WallAdmin(admin.ModelAdmin):
    list_display = ['__str__','owner','availabale','active']

    class Meta :
        model = Wall

admin.site.register(Wall,WallAdmin)