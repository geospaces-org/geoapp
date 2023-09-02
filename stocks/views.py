import os, json

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
BASE         = "/opt/data/data/stocks/data"
DEFAULT_LIST = None
DEFAULT_FILE = f'{BASE}/stocks.csv'
def reload(request, **kwargs):
    global DEFAULT_LIST
    DEFAULT_LIST = None
    print("RESET the DEFAULT LIST ...")
    return getSymbols(request, **kwargs)

def getSymbols(request, **kwargs):
    global DEFAULT_LIST
    parms = mango.getparms(request)
    user = parms.get("user", "")
    file = f'{BASE}/{user}/stocks.csv'

    print(f"Symbols List user:{user} - {DEFAULT_FILE}")
    if (not user or not os.path.exists(file)):
        _, ret = read_csv(DEFAULT_FILE)
        DEFAULT_LIST = json.dumps(ret)
        print(f"DEFAULT List user:{user} - {DEFAULT_LIST}")
        return HttpResponse( DEFAULT_LIST)
    else:
        _, ret = read_csv(file)
        return HttpResponse( json.dumps(ret))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def getDetails(request, **kwargs):
    global DEFAULT_LIST
    parms = mango.getparms(request)
    symbol= parms.get("q"       , "dow_jones").lower()
    timed = parms.get("duration", "all")

    csv     = f'{BASE}/{symbol}/daily.csv'
    csv_aug = f'{BASE}/{symbol}/daily_aug.csv'

    if os.path.exists(csv_aug):
        csv = csv_aug
    elif ( not os.path.exists(csv  )):
        csv   = f'{BASE}/dow_jones/daily.csv'

    news    = f'{BASE}/{symbol}/news.html'
    stats1  = f'{BASE}/{symbol}/summary.json'
    stats2  = f'{BASE}/{symbol}/fundamentals.json'

    if (not os.path.exists(news  )): news  = f'{BASE}/dow_jones/news.html'
    if (not os.path.exists(stats1)): stats1= f'{BASE}/dow_jones/summary.json'

    s1 = json.loads(readfile(stats1, "{}"))
    s2 = json.loads(readfile(stats2, "{}"))
    s2.update(s1)

    print(f"Symbol Details :{csv} - {news} {stats1}")

    df, ret = read_csv(csv)
    ret['news'] = readfile(news, "")
    ret['stats']= json.dumps(s2)

    return HttpResponse( json.dumps(ret))
'''

