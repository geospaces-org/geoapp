from django.shortcuts import render
import apps.settings

APPNAME   ='geoapp'

# -----------------------------------------------------------------------
def index(request):
    if (not apps.settings.DEFAULT_APP ):
        return render(request, 'index.html')
        
    app = f'{apps.settings.DEFAULT_APP}'
    return render(request, f'{app}/index.html/' )

# -----------------------------------------------------------------------

