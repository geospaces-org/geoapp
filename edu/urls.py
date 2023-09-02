from django.urls import path, include
from . import views
from mangorest import mango

app_name = 'edu'

urlpatterns = [
    path(r'edu/'      , views.index , name='Put Files'),
]
