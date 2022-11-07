from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from mangorest import mango
import apps.settings

app_name = 'geoapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path(r'', views.index, name='index'),
] + apps.settings.INSTALLED_URLS + [
    re_path(r'^.*/$', mango.Common, name='catchall'),
]
urlpatterns = staticfiles_urlpatterns() + urlpatterns
