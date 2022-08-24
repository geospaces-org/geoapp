from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from mangorest import mango

app_name = 'geoapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path(r'', views.index, name='index'),
    path(r'geoapp/', views.index, name='index'),

    url(r'^.*/$', mango.Common, name='catchall'),
]
urlpatterns = staticfiles_urlpatterns() + urlpatterns
