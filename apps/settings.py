DEFAULT_APP = "tseries"

'''
You can include this in your html pages and refer to these variables:
For example:

	{{ appname }}

'''
#---------------------------------------------------------------------------------
import logging
loga = logging.getLogger( "app.analytics")

fh = logging.FileHandler("/tmp/geo_analytics.log")
sh = logging.StreamHandler()
#vars(sh)
fmt = logging.Formatter(fmt='%(asctime)-12s,%(message)s', datefmt='%Y-%m-%dT%H:%M:%S' )
sh.setFormatter(fmt) 
fh.setFormatter(fmt)
#loga.addHandler(sh)
loga.addHandler(fh)

loga.info(f"#time,user,uri,method,REMOTE_ADDR")
def analytics(r):
    out = f"{r.user},{r.build_absolute_uri()},{r.META['REQUEST_METHOD']},{r.META['REMOTE_ADDR']}"
    loga.info(f"{out}")
#---------------------------------------------------------------------------------
def appcontext(request):
    context = {
        "appname": "STREAM",
        "weburl" : "https://stream.geospaces.org/",
        "top_url": "tseries/topbar.html",
		"SSO" : 1 # Set to 0 to disable SSO
    }
    analytics(request)
    return context
