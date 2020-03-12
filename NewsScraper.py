import feedparser
import urllib
import json
import pprint
import sys
import csv

#arg = sys.arg[1]

#convert keyword to url encoding
s = '自動車'
s_quote = urllib.parse.quote(s)

#insert keyword into google news url
url = "https://news.google.com/news/rss/search/section/q/" + s_quote + "/" + s_quote + "?ned=jp&amp;hl=ja&amp;gl=JP"

#parse newsfeed
d = feedparser.parse(url)
news = list()

for i, entry in enumerate(d.entries, 1):
    p = entry.published_parsed
    sortkey = "%04d%02d%02d%02d%02d%02d" % (p.tm_year, p.tm_mon, p.tm_mday, p.tm_hour, p.tm_min, p.tm_sec)
    tmp = {
        "no" : i,
        "title" : entry.title,
        "summery" : entry.summary,
        "link" : entry.link,
        "published" : entry.published,
        "sortkey" : sortkey
    }

    news.append(tmp)

pprint.pprint(news[0:2])

#open csv file with date
#with open('AutoNews.json', 'w') as f:
#    json.dump(news, f)

#insert news