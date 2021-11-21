from django.urls import path
from.views import user_profile
urlpatterns = [

    path('user-profile',user_profile),
    #path('',include('accounts.urls')),
    #path('admin/', admin.site.urls),
]
