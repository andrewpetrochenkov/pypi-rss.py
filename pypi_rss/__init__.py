from datetime import datetime
import time
import xmltodict
import requests_retry_on_exceptions as requests

def getdatetime(string):
    local_time = time.strptime(string, '%a, %d %b %Y %H:%M:%S GMT')
    local_seconds = time.mktime(local_time)
    utc_timestamp = time.gmtime(local_seconds)
    return datetime.fromtimestamp(time.mktime(utc_timestamp))

def get_items(url):
    try:
        r = requests.get(url,timeout=5)
        return xmltodict.parse(r.text)['rss']['channel']['item']
    except: # requests/xml exceptions. shit happens
        return []

def get_newest_packages(url=None):
    items = []
    for item in get_items(url if url else "https://pypi.org/rss/packages.xml"):
        title = item['title']
        pubdate = getdatetime(item['pubDate'])
        name = title.split(' ')[0]
        items.append(dict(title=title,pubdate=pubdate,name=name))
    return items

def get_latest_updates(url=None):
    items = []
    for item in get_items(url if url else "https://pypi.org/rss/updates.xml"):
        title = item['title']
        pubdate = getdatetime(item['pubDate'])
        name, version = title.split(' ')
        items.append(dict(title=title,pubdate=pubdate,name=name,version=version))
    return items

