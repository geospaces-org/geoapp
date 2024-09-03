DEFAULT_APP = "geospaces"

'''
You can include this in your html pages and refer to these variables:
For example:

	{{ appname }}

'''
import geoapp.analytics as analytics
#---------------------------------------------------------------------------------
def appcontext(request):
    context = {
        "appname": "Geo Spaces",
        "weburl" : "https://www.geospaces.org/",
        "top_url": "geospaces/topbar.html",
		"SSO": 0,
        "NO_LOGIN_MENU": 1,
        "NO_APP_MENU" : 1
    }    
    analytics.loganalytics(request);
    
    return context
