#!/usr/bin/env python 

#*** DO NOT EDIT - GENERATED FROM services.ipynb ****

import os, json, sys, datetime, geoapp, aiservices, logging
from  mangorest.mango import webapi
import aiservices

BASE = "/opt/data/data/articles/raw/"
logger = logging.getLogger( "app.blogs")

#--------------------------------------------------------------------------------------------------------
DIRS = ("blogs/static/blogs/data/", "static/docs/", BASE)

def find(file, dirs=DIRS):
    if os.path.exists(file):
        return file
    for d in dirs:
        f = os.path.join(d, file)
        if os.path.exists(f):
            return f
    return None
#--------------------------------------------------------------------------------------------------------
@webapi("/blogs/getarticle")
def getarticle(request, file="", viewid="", dirs=DIRS, **kwargs):
    file = file or viewid
    f = find(file)
    if (not f):
        return f'{file} - does not exist!!!';

    cont = geoapp.utils.readfile(f )
    meta = json.loads(geoapp.utils.readfile(f+".meta", "{}"))
    title= meta.get('title', '')

    ret = { "title": title, "content": cont , "meta": meta, "dir": os.path.dirname(f) }
    return json.dumps(ret)
#--------------------------------------------------------------------------------------------------------    
@webapi("/blogs/createarticle")
def article(request, user="noname", cfilename="", title="", contents="", **kwargs):
    if (not cfilename):
        cfilename = f"{user}-{datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S')}.md"
#--------------------------------------------------------------------------------------------------------    
@webapi("/blogs/savearticle")
def savearticle(request, user="noname", cfilename="", title="", contents="", **kwargs):
    if (not contents):
        return "No contents!!"

    file = find(cfilename)
    if (not file):
        if (not cfilename):
            file = f"{user}-{datetime.datetime.utcnow().replace(microsecond=0).isoformat()}.md"
        else:
            file = DIRS[0] + cfilename

    logger.info(f"===> Saving {file} ...")
    indexed = file+".mdd"
    if os.path.exists(indexed):
        os.remove(indexed)

    meta = file+".meta"
    if os.path.exists(meta):
        os.remove(meta)

    dirn = os.path.dirname(cfilename)
    if(not os.path.exists(dirn) ): 
        os.makedirs( dirn ) 

    # Upload file attachments if any
    files = geoapp.utils.uploadFiles(request )
    kwargs['files']    = files
    kwargs["filename"] = cfilename
    kwargs["title"]    = title
    kwargs["user"]     = user
    kwargs["date"]     = f"{datetime.datetime.utcnow()}" 

    with open(meta, "w") as f:
        f.write(json.dumps(kwargs, indent = 4) )

    with open(cfilename, "wb") as f:
        f.write(contents.encode('utf-8'))

    #os.system('/opt/utils/filestoes.py -d "/opt/data/data/articles/raw" -t "*.md" &')
        
    return f'Saved: {json.dumps(kwargs, indent = 4)} '
