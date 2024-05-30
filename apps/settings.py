DEFAULT_APP = "edu"

'''
You can include this in your html pages and refer to these variables:
For example:
	{{ appname }}
'''
#---------------------------------------------------------------------------------
def appcontext(request):
    context = {
        "appname": "AI University",
        "weburl" : "https://www.geospaces.org/",
        "top_url": "edu/topbar.html",
        "SSO": 0
    }
    
    return context
