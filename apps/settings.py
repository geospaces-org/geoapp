DEFAULT_APP = "example_app"

'''
You can include this in your html pages and refer to these variables:
For example:

	{{ appname }}

'''
import geoapp.analytics as analytics
#---------------------------------------------------------------------------------
def appcontext(request):
    context = {
        "appname": "ExAmPlE",
        "weburl" : "https://www.geospaces.org/",
        "top_url": "example_app/topbar.html",
		"SSO": 1
    }    
    analytics.loganalytics(request);
    
    return context
