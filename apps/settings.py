from django.urls import path, include, re_path


DEFAULT_APP = "tseries"

'''
You can include this in your html pages and refer to these variables:
For example:

	{{ appname }}

'''
#---------------------------------------------------------------------------------
def appcontext(request):
    context = {
        "appname": "GEOSPACE APPLICATION",
        "weburl" : "https://www.geospaces.org/"
    }
    
    return context


