#!/usr/bin/python
import sys
from urllib2 import Request, urlopen, URLError
import json
import geocoder

def print_5prayer_times(adhan_times,my_city,my_country):
    print " Prayer time for "+my_city+", "+my_country+" :\n",\
        " Fajr "+adhan_times['data']['timings']['Fajr']+"\n",\
        " Dhuhr "+adhan_times['data']['timings']['Dhuhr']+"\n",\
        " Asr "+adhan_times['data']['timings']['Asr']+"\n",\
        " Maghrib "+adhan_times['data']['timings']['Maghrib']+"\n",\
        " Isha "+adhan_times['data']['timings']['Isha']+"\n",\


def main(argv):
        if(len(argv)>1):
            # calling by 'script -c city'
            if((argv[0]=="-c")|(argv[0]=="--city")):
                try:
                    my_country = geocoder.google(argv[1]).country
                    my_city = geocoder.google(argv[1]).city
                    request = Request("http://api.aladhan.com/timingsByCity?city="+my_city+"&country="+my_country+"&method=3")
                    response = urlopen(request)
                    answer = response.read()
                    adhan_times = json.loads(answer)
                    print_5prayer_times(adhan_times,my_city,my_country)
                except URLError, e:
                    print "No responses, error"

        else:
            try:
                #Get my current location
                my_country = geocoder.ip('me').country
                my_city = geocoder.ip('me').city
                #Call AlAdhan API
                request = Request("http://api.aladhan.com/timingsByCity?city="+my_city+"&country="+ my_country+"&method=3")
                response = urlopen(request)
                answer = response.read()
                adhan_times = json.loads(answer)
                #Print 5 prayer times
                print_5prayer_times(adhan_times,my_city,my_country)
            except URLError, e:
                print "No responses, error"


if __name__ == '__main__':
    main(sys.argv[1:])
