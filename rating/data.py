import urllib2
import json


def get_data(app_id, page=1):
    response = urllib2.urlopen(
        'https://itunes.apple.com/rss/customerreviews/page=' + str(page) + '/id=' + str(
            app_id) + '/sortby=mostrecent/json?l=en&&cc=cn')
    if not response.getcode() == 200:
        return ""
    data = response.read().decode('utf-8')
    jsonb = json.loads(data)
    feed = jsonb.get('feed')
    href = feed.get('link')[3].get('attributes').get('href')

    start = href.find('=') + 1
    end = href[start:].find('/')
    p = href[start:start + end]
    print 'start:%s , end:%s , p:%s' % (start, end, p)
    entry = get_data_page(app_id, page, int(p))
    re = r'{"entry":' + json.dumps(entry) + '}'
    return re


def get_data_page(app_id, page=1, count=1):
    response = urllib2.urlopen(
        'https://itunes.apple.com/rss/customerreviews/page=' + str(page) + '/id=' + str(
            app_id) + '/sortby=mostrecent/json?l=en&&cc=cn')
    if not response.getcode() == 200:
        return ""
    data = response.read().decode('utf-8')
    jsonb = json.loads(data)
    entry = jsonb.get('feed').get('entry')
    entry.pop(0)
    if page < count:
        entry.extend(get_data_page(app_id, page + 1, count))
    return entry
