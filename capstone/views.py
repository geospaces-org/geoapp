from django.shortcuts import render

def index(request):
    #Check if shopping cart has items
    return render(request, 'capstone/index.html')
