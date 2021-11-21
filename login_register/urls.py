from django.urls import path
from .views import *

urlpatterns = [
    path('login',login_user_page),
    path('register',register_user_page)
]