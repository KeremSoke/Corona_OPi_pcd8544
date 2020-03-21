#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup as bsoup
import bs4 as bs
import urllib2,cookielib
import time
import OPi_pcd8544.lcd as lcd
import os
import sys

if not os.geteuid() == 0:
    sys.exit('!Script must be run as root!')

site= "https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Turkey" #Wikipedia Address
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

lcd.init()
lcd.cls()
time.sleep(2)
while True:
    lcd.centre_text(5," Yukleniyor") #loading
    req = urllib2.Request(site, headers=hdr)
    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()

    content = page.read()
    soup = bsoup(content,'lxml')
    table = soup.find('table', class_="infobox")
    table_rows = table.find_all('tr')
    a = 0
    lcd.cls()
    for tr in table_rows:
        td = tr.find_all('td')
        for i in td:
            if a == 6:
                inpt = str(i.text)
                print inpt.split("[")[0]
                confirmed = inpt.split("[")[0]
            if a == 7:
                inpt = str(i.text)
                print inpt.split("[")[0]
                cured = inpt.split("[")[0]
            if a == 8:
                inpt = str(i.text)
                print inpt.split("[")[0]
                dead = inpt.split("[")[0]
            else:
                pass
        a = a+1
    lcd.centre_text(0, "Hasta: " + confirmed) #cofirmed
    lcd.centre_text(2, "Kurtulan: " + cured)	#cured
    lcd.centre_text(4, "   Olu: " + dead) #dead
    time.sleep(180)
    lcd.cls()
	
