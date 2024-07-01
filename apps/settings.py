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

loga.info(f"#time,user,uri,REQUEST_METHOD,REMOTE_ADDR,REMOTE_HOST,SERVER_NAME")
def analytics(r):
    #out  = r.user + .username if r.user.is_authenticated() else '' 
    #out += "," + r.getRequestURI() + ","
    out = f"{r.user},{r.build_absolute_uri()}"
    for c in ['REQUEST_METHOD','REMOTE_ADDR', 'REMOTE_HOST','SERVER_NAME']:
        out += r.META[c] + ","

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
