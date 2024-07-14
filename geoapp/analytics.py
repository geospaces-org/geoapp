#!/usr/bin/env python
'''
    GENERATED FROM geoapp/notebooks/analytics.ipynb
'''
##---------------------------------------------------------------------
import os, logging, sys
import colabexts.utils as colabexts_utils

loga  = logging.getLogger( "app.analytics")

file  = "/opt/data/tseries/data/_ANALYTICS/analytics.log"
if  not os.path.exists(os.path.dirname(file)) :
    os.makedirs(os.path.dirname(file))
    
fmt   = logging.Formatter(fmt='%(message)s,%(asctime)-12s', datefmt='%Y-%m-%dT%H:%M:%S' )
fileh = logging.FileHandler(file)
fileh.setFormatter(fmt)
loga.addHandler(fileh)
loga.propagate = False

__ADD_STREAM__ = 0
if __ADD_STREAM__:
    sh = logging.StreamHandler()
    sh.setFormatter(fmt) 
    loga.addHandler(sh)

loga.info(f"#user,uri,method,REMOTE_ADDR,time")

def loganalytics(r):
    try:
        uri,reqm,remt = r.build_absolute_uri(), r.META.get('REQUEST_METHOD',''), \
                        r.META.get('REMOTE_ADDR','')
    except:
        uri,reqm,remt =  "URI", "method", "remote-ip"
        pass

    out = f"{r.user},{uri},{reqm},{remt}"
    loga.error(f"{out}")

if __name__ == '__main__' or colabexts_utils.inJupyter():
    pass
