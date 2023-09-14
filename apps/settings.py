DEFAULT_APP = "tseries"

'''
You can include this in your html pages and refer to these variables:
For example:

	{{ appname }}

'''
#---------------------------------------------------------------------------------
def appcontext(request):
    context = {
        "appname": "STREAM",
        "weburl" : "https://stream.geospaces.org/",
        "top_url": "tseries/topbar.html"
    }    
    return context
