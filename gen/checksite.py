#!/usr/local/bin/python

import datetime, requests, time, sys, os
from django.core.mail import send_mail
from django.conf import settings
sys.path.append(os.path.expanduser("~/.django") )
import my_config

if ( not settings.configured):
    settings.configure(
        EMAIL_USE_TLS       = my_config.EMAIL_USE_TLS       ,
        EMAIL_HOST          = my_config.EMAIL_HOST          ,
        EMAIL_PORT          = my_config.EMAIL_PORT          ,
        DEFAULT_FROM_EMAIL  = my_config.DEFAULT_FROM_EMAIL  ,
        EMAIL_HOST_USER     = my_config.EMAIL_HOST_USER     ,
        EMAIL_HOST_PASSWORD = my_config.EMAIL_HOST_PASSWORD ,
        EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
    )

def sendMail(to="sada@geospaces.org", subject="hello", msg="Check server!"):
    r = [f.strip() for f in to.split(",")]

    try:
        ret = send_mail( from_email= settings.DEFAULT_FROM_EMAIL, subject=subject, message=msg, recipient_list=r,fail_silently = False)
    except Exception as e:
        print("ERROR: ", e)

    print(f'Sending Emails to {r} {ret}')
    
    
def fixsite(s=""):
    print(f"+++++ Fixing Site: {s}")
    SSHC = os.path.expanduser("~/ec2-keys/du1.sh")
    out=subprocess.run([SSHC, "start.sh"],  capture_output=True)
    o=out.stdout.decode("utf-8")
    
    out=subprocess.run([cmd1, "screen -ls"],  capture_output=True)
    o=out.stdout.decode("utf-8")
    print("+++++ Fixing ", o)

    
def main(site="https://www.geospaces.org"):
    r, i = None, 0
    print( f"?: {datetime.datetime.now()}:  ", end="")
    try:
        r = requests.get(site)
        if ( r.status_code == 200):
            txt = {r.text[0:60].replace('\n', '<NL>')}
            print(f"+ {r.status_code} : {txt} ...")
    except Exception as e:
        print( f"ERROR: {e}")
        r = None
        
    if ( r is None):
        print(f"ERROR:  Fixing ...")
        sendMail("sada@geospaces.org", f"{site} Down", f"Checking {site} ")
        fixsite(s)
    
#----------------------------------------------------------------------------------
def inJupyter():
    try:    get_ipython; return True
    except: return False
    
if __name__ == '__main__' and not inJupyter():
    main("https://www.geospaces.org")
    pass
