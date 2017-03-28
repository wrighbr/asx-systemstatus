from bs4 import BeautifulSoup
import urllib2, gzip, StringIO

systems = 'ASX+Trade','ASX24+(NTP)','Chess','Austraclear','Genium','Calypso+(OTC+Clearing)','ASX+Collateral','DCS',\
          'ASX+Online','Test+Systems','Supporting+Services+and+Platforms'
systemtidy = []
systemstatus = []

for system in systems:
    url = 'https://pub.s7.exacttarget.com/0b0bg154xcs?SystemName='+system

    response = urllib2.urlopen(url)
    html = response.read()

    data = StringIO.StringIO(html)
    gzipper = gzip.GzipFile(fileobj=data)
    html = gzipper.read()
    soup = BeautifulSoup(html, 'html.parser')

    system = system.replace('+', ' ')
    systemtidy.append(system)

    status = soup.find_all('li')
    status = str(status).replace('[<li class="status ', '')
    status = status.replace('"></li>]','')

    systemstatus.append(status)

layout = "{!s:35} {!s:5}"

print(layout.format('System','Status'))
print(layout.format('------','------'))

for a,b in zip(systemtidy, systemstatus):
    print(layout.format(a,b))