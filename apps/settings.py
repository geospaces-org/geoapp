DEFAULT_APP = "geospaces"

'''
You can include this in your html pages and refer to these variables:
For example:

	{{ appname }}

'''
#---------------------------------------------------------------------------------
def appcontext(request):
    context = {
        "appname": "Example Application",
        "weburl" : "https://www.geospaces.org/",
        "top_url": "geospaces/topbar.html"
        "SSO": 0
    }
    
    return context


