from django.contrib import admin
from django.urls import path
from .views import get_even,get_odd,get_fibo,get_rand
urlpatterns = [
    path('get_eve',get_even),
    path('get_odd',get_odd),
    path('get_fibo',get_fibo),
    path('get_rand',get_rand),
    
]