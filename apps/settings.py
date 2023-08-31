DEFAULT_APP = "example_app"

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
        "top_url": "example_app/topbar.html"
    }
    
    return context


