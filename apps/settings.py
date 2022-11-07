from django.urls import path, include, re_path


DEFAULT_APP = 'tseries'

INSTALLED_APPS = [
    'tseries',
]

INSTALLED_URLS = [
    path('tseries/', include('tseries.urls'), name="tseries"),
]

