#!/usr/bin/python
from urllib2 import Request, urlopen, URLError
import json
request = Request("http://api.aladhan.com/timingsByCity?city=Oran&country=DZ&method=3")

try:
    response = urlopen(request)
    answer = response.read()
    adhan_times = json.loads(answer)
except URLError, e:
    print "No responses, error"

print " Fajr "+adhan_times['data']['timings']['Fajr']+"\n",\
    " Dhuhr "+adhan_times['data']['timings']['Dhuhr']+"\n",\
    " Asr "+adhan_times['data']['timings']['Asr']+"\n",\
    " Maghrib "+adhan_times['data']['timings']['Maghrib']+"\n",\
    " Isha "+adhan_times['data']['timings']['Isha']+"\n",\
