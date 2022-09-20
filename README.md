# Application Template

Use this as a generic template for the applications. To install you application, use a git repo to develop your application.
Once done add it to


## Basic setup


* Link tseries directory to /opt/data/tseries
> ln -s /opt/LMCO/git/notebooks/DS/tseries/db/ /opt/data/tseries/db

You must create a ~/.myconfig with collowing contents - 
replace with meaningful results:

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.yourdomain.com'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'yourusername'
EMAIL_HOST_USER = 'yourhost'
EMAIL_HOST_PASSWORD = 'password$'
SECRET_KEY="yoursecret key"
ENV='local|production'
STRIPE_PUBLIC_TEST='A'
STRIPE_SECRET_TEST='A'
STRIPE_PUBLIC_LIVE='B'
STRIPE_SECRET_LIVE='B'
STRIPE_PUBLIC = STRIPE_PUBLIC_LIVE
STRIPE_SECRET = STRIPE_SECRET_LIVE
CAPTCHA_SITE   = 'key'
CAPTCHA_SECRET = 'key'

---

## To install new application

assume you are adding application named 'mvideo' 

* geoapp/settings.py
- Add a line to 'INSTALLED_APPS'
>> INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'mvideo'
    ]

* geoapp/urls.py - add the following line 
    path('mvideo/',   include('mvideo.urls'),   name="mvideo"),
