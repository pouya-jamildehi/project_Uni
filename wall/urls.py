from django.urls import path
from.views import add_wall
urlpatterns = [

    path('add-wall',add_wall),
    #path('',include('accounts.urls')),
    #path('admin/', admin.site.urls),
]
