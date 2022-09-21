import re
import urllib
from urllib.parse import urlsplit
from urllib.request import urlopen

from bs4 import BeautifulSoup

hashmap = {}


def getExt(urls):
    for url in urls:
        o = urllib.parse.urlsplit(url)
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')
        for link in bs.find_all('a', href=re.compile('^((https://)|(http://))')):
            if 'href' in link.attrs:
                if o.netloc in (link.attrs['href']):
                    continue
                else:
                    hashmap[url] = hashmap.get(url, 0) + 1
    for url in hashmap:
        print(url + " " + str(hashmap[url]))


getExt(['https://stackoverflow.com/', "https://www.vox.com/", "https://en.wikipedia.org/wiki/Computer_programming"])