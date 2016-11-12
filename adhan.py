#!/usr/bin/python
import sys, getopt
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

def display_help():
    print """
Help:
    -c, --city [city name]
    show by city
  """


def main(argv):
        if(len(argv)>=1):
            try:
                # calling by 'script -c city'
                opts, args = getopt.getopt(argv, 'hc:', ['city='])
            except getopt.GetoptError:
                print "Error for help type  adhan.py help"
            for opt,args in opts:
                if opt == '-h':
                    display_help()
                elif opt in ('-c','--city'):
                    try:
                        my_country = geocoder.google(args).country
                        my_city = geocoder.google(args).city
                        request = Request("http://api.aladhan.com/timingsByCity?city="+my_city+"&country="+my_country+"&method=3")
                    except Exception as e:
                        print "No responses, please check your city name"
                    else:
                        response = urlopen(request)
                        answer = response.read()
                        adhan_times = json.loads(answer)
                        print_5prayer_times(adhan_times,my_city,my_country)
        else:
            try:
                #Get my current location
                my_country = geocoder.ip('me').country
                my_city = geocoder.ip('me').city
                #Call AlAdhan API
                request = Request("http://api.aladhan.com/timingsByCity?city="+my_city+"&country="+ my_country+"&method=3")
            except Exception as e:
                print "No responses, error"
            else:
                response = urlopen(request)
                answer = response.read()
                adhan_times = json.loads(answer)
                #Print 5 prayer times
                print_5prayer_times(adhan_times,my_city,my_country)
if __name__ == '__main__':
    main(sys.argv[1:])
