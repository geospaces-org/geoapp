from django.urls import path, include
from django.conf.urls import include, url


DEFAULT_APP = 'tseries'

INSTALLED_APPS = [
    'tseries',
]

INSTALLED_URLS = [
    path('tseries/', include('tseries.urls'), name="tseries"),
]

