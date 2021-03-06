#!/usr/bin/python
# -*- coding:Utf-8 -*-

import urllib2
from django.conf import settings

PARLTRACK_URL = settings.PARLTRACK_URL

current_meps = "/meps/?format=json"

def get_data():
    return urllib2.urlopen(PARLTRACK_URL + current_meps).read()

if __name__ == "__main__":
    open("meps.json", "w").write(get_data())
    print "current meps successfully downloaded"

# vim:set shiftwidth=4 tabstop=4 expandtab:
