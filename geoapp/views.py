from django.shortcuts import render

APPNAME   ='geoapp'

def index(request):
    return render(request, 'index.html')
