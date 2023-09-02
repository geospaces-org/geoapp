#!/usr/local/bin/python 

#*** DO NOT EDIT - GENERATED FROM services.ipynb ****

import os
import pandas as pd
from  mangorest.mango import webapi

BASE = "/opt/data/capstone/capstone"

#--------------------------------------------------------------------------------------------------------    
def getFile(path, ret=""):

    print(f"==> getFile: {path}")
    if (os.path.exists(path)):
        with open(path, "r") as f:
            ret = f.read()

    return ret
#--------------------------------------------------------------------------------------------------------    
@webapi("/capstone/test")
def test( request,  **kwargs):
    return "APP 1 TEST version 1.0"
#--------------------------------------------------------------------------------------------------------    
DEFAULT_MENU = '''
# Home              ; fa fa-home          ;; Home ;

# Find FA ICON      ; fas fa-fan          ;; find-fa-icon       ;; Match find a FA Icon
# Face Recognition  ; far fa-meh          ;; facial_recognition ;; Face Recognition system
# Return to Kronos  ; fas fa-shuttle-van  ;; ReturntoKronos     ;; Return to Kronos
---
# About             ; fas fa-book-reader  ;;                    ;;
# Donate            ; fas fa-donate       ;/payment/stripepay/donate/ ; 
'''
@webapi("/capstone/capmenu")
def capmenu(request, **kwargs):
    ret = getFile(f'{BASE}/capmenu.md', DEFAULT_MENU)
    return ret

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@webapi("/capstone/getcapstone")
def getcapstone(request, q, **kwargs):
    bq = f'{BASE}/{q}'

    if (not os.path.exists(bq)):
        ret = f"ERROR: '{bq}' path does not exist!!"
        print(ret)
        return HttpResponse( ret)

    descr = "<html>Not available here - run scripts!! </html>"
    overv = getFile(f'{bq}/README.md',    descr)
    datah = getFile(f'{bq}/data.md' ,     descr)
    soluh = getFile(f'{bq}/solutions.md', descr)
    discs = getFile(f'{bq}/discuss.md'  , descr)

    ret = {
        "img"         : "",
        "overview"    : overv,
        "data"        : datah,
        "solutions"   : soluh,
        "discussions" : discs,
    }
    return ret
