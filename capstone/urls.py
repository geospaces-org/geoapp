from django.urls import path
from . import views

app_name = 'capstone'

urlpatterns = [
    path('',  views.index , name='capstone projects'),
    path('capstone/',  views.index , name='capstone projects'),
]
