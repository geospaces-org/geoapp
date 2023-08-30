#DEFAULT_APP = "tseries"

'''
You can include this in your html pages and refer to these variables:
For example:

	{{ appname }}

'''
#---------------------------------------------------------------------------------
def appcontext(request):
    context = {
        "appname": "GeoSpaces",
        "weburl" : "https://www.geospaces.org/",
        #"top_url": "topbar.html"
    }
    
    return context


