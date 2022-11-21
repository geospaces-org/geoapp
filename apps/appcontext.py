# appcontext.py
# Any context related to geoapp must be included here

'''
You can include this in your html pages and refer to these variables:

Fro example:

{{ appcontext.appname }}

'''


#---------------------------------------------------------------------------------
def appcontext(request):
    context = {
        "appname": "GEOSPACE APPLICATION",
        "weburl" : "https://www.geospaces.org/"
    }
    
    return context
