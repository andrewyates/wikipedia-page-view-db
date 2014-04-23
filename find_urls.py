# find pagecount files to download
import datetime
import re
import time

import requests
from bs4 import BeautifulSoup
from django.utils.timezone import utc

from orm.models import PagecountURL

headers = {'User-agent': 'wikipedia-page-view-db'}


def main():
    base = 'http://dumps.wikimedia.org/other/pagecounts-raw'

    for year in range(2007, datetime.date.today().year + 1):
        r = requests.get("%s/%s" % (base, year), headers=headers)
        print year
        soup = BeautifulSoup(r.content)

        for a in soup.find_all('a'):
            if re.match("^[0-9]{4}-[0-9]{2}$", a['href']) is not None:
                add_file_links("%s/%s/%s" % (base, year, a['href']))
                time.sleep(0.25)

        time.sleep(1)


def add_file_links(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content)

    for a in soup.find_all('a'):
        if a['href'].startswith("pagecounts-"):
            pcurl = "%s/%s" % (url, a['href'])

            if PagecountURL.objects.filter(url=pcurl).exists():
                continue

            pcu = PagecountURL.objects.create(url=pcurl, retrieved=False, time=parse_time(a['href']))
            pcu.save()
            print pcu.time


def parse_time(s):
    _, d, t = s.replace(".gz", "").split("-")
    return datetime.datetime.strptime("%s %s UTC" % (d, t), "%Y%m%d %H%M%S %Z").replace(tzinfo=utc)

if __name__ == "__main__":
    main()
