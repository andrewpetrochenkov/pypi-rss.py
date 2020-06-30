__all__ = ['get_pubdate', 'get_items',
           'get_newest_packages', 'get_latest_updates']


from datetime import datetime
import time
import xmltodict
import requests_retry_on_exceptions as requests


def get_pubdate(string):
    local_time = time.strptime(string, '%a, %d %b %Y %H:%M:%S GMT')
    local_seconds = time.mktime(local_time)
    utc_timestamp = time.gmtime(local_seconds)
    return datetime.fromtimestamp(time.mktime(utc_timestamp))


def get_items(url):
    try:
        r = requests.get(url, timeout=5)
        return xmltodict.parse(r.text)['rss']['channel']['item']
    except:  # requests/xml exceptions. shit happens
        return []


def get_newest_packages(url=None):
    items = []
    for item in get_items(url if url else "https://pypi.org/rss/packages.xml"):
        items.append(dict(
            title=item['title'],
            link=item['link'],
            guid=item['guid'],
            description=item.get('description', None),
            author=item.get('author', None),
            pubdate=get_pubdate(item['pubDate']),
            name=item['title'].split(' ')[0]
        ))
    return items


def get_latest_updates(url=None):
    items = []
    for item in get_items(url if url else "https://pypi.org/rss/updates.xml"):
        items.append(dict(
            title=item['title'],
            link=item['link'],
            description=item.get('description', None),
            author=item.get('author', None),
            pubdate=get_pubdate(item['pubDate']),
            name=item['title'].split(' ')[0],
            version=item['title'].split(' ')[1]
        ))
    return items
