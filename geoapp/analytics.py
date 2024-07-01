#!/usr/bin/env python
'''
    GENERATED FROM geoapp/notebooks/analytics.ipynb
'''
##---------------------------------------------------------------------
import logging, sys
import colabexts.utils as colabexts_utils

loga  = logging.getLogger( "stream.analytics")
for handler in loga.handlers: 
    loga.removeHandler(handler)
loga.handlers.clear()

fmt   = logging.Formatter(fmt='%(message)s,%(asctime)-12s', datefmt='%Y-%m-%dT%H:%M:%S' )
fileh = logging.FileHandler("/tmp/stream_analytics.log")
fileh.setFormatter(fmt)
loga.addHandler(fileh)
loga.propagate = False

__ADD_STREAM__ = 0
if __ADD_STREAM__:
    sh = logging.StreamHandler()
    sh.setFormatter(fmt) 
    loga.addHandler(sh)

loga.info(f"#time,user,uri,method,REMOTE_ADDR")

def analytics(r):
    global loga
    try:
        uri,reqm,remt = r.build_absolute_uri(), r.META.get('REQUEST_METHOD',''), \
                        r.META.get('REMOTE_ADDR','')
    except:
        uri,reqm,remt =  "URI", "method", "remote-ip"
        pass

    out = f"{r.user},{uri},{reqm},{remt}"
    loga.info(f"{out}")

if __name__ == '__main__' or colabexts_utils.inJupyter():
    pass
