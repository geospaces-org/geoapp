from django.urls import path
from . import views

app_name = 'geospaces'

urlpatterns = [
    path('LINK/',  views.index , name='geospaces urls1'),
]
