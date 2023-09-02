from django.shortcuts import render

APPNAME   ='edu'

def index(request):
    return render(request, 'index.html')
