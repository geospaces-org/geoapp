DEFAULT_APP = "tseries"

'''
You can include this in your html pages and refer to these variables:
For example:

	{{ appname }}

'''
import geoapp.analytics as analytics
#---------------------------------------------------------------------------------
def appcontext(request):
    context = {
        "appname": "STREAM",
        "weburl" : "https://stream.geospaces.org/",
        "top_url": "tseries/topbar.html",
		"SSO": 1
    }    
    analytics.loganalytics(request);
    
    return context
