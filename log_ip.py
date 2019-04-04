# log internal ip's from (2) sources: ipconfig, upnpc
# log external ip's from (4) sources: urllib, curl, dig, upnpc
# print these into formatted columns for comparison
from subprocess import *
import subprocess
import datetime
import socket
import urllib.request
import json
import re

def printer(list):
    file = open('/Users/mattmcmahon/Desktop/Scripts/ip-log1.nosync', 'a')
    
    for i,el in enumerate(list):
        if (i == 0 or i == 9):
            el = el[0:14]
            el = '{:^14}'.format(el)
            file.write('|' + el)
        elif (i == 1):
            el = el[0:11]
            el = '{:^11}'.format(el)
            file.write('|' + el)
        elif (i == 8):
            el = el[0:25]
            el = '{:^25}'.format(el)
            file.write('|' + el)
        elif (i == 10):
            el = el[0:16]
            el = '{:^16}'.format(el)
            file.write('|' + el)
        elif (i == 11):
            el = el[0:18]
            if ("----" not in el):
                el = '{:^17}'.format(el)
                file.write('|' + el + "|")
            else:
                el = '{:^18}'.format(el)
                file.write('|' + el)
        elif (i == 2):
            el = el[0:18]
            el = '{:^17}'.format(el)
            file.write('|' + el)
        else:
            el = el[0:17]
            el = '{:^17}'.format(el)
            file.write('|' + el)

    file.write("\n")
    file.close()


# example for formating:
title = ['date', 'time', 'SSID','ext: urllib', 'ext: curl', 'ext: dig', 'ext: upnpc', 'internal', 'sock_hostname', 'latitude', 'longitude', 'city']
lines = ['--------------', '-----------', '-----------------', '-----------------', '-----------------', '-----------------', '-----------------', '-----------------', '-------------------------', '--------------', '----------------', '-----------------|']
dt = tt = urlib = cur = dig = pnp = ipconfig = sock_name = lat = lon = city = "test"
ssid = "-------------------"

# printer(lines)
# printer(title)
# printer(lines)

dt = datetime.datetime.now().strftime("%b.%d.%Y")
tt = datetime.datetime.now().strftime("%H:%M:%S")

try:
    ssid = Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'], stdout=PIPE, stderr=PIPE)
    ssid, err = ssid.communicate()
    ssid = ssid.decode('utf-8')
    for i,el in enumerate(ssid.split()):
        if(el == "SSID:"):
            ssid = (ssid.split()[i + 1])
except:
    ssid = "Error"
    print(ssid)

try:
    sock_name = socket.gethostname()
    ipconfig = socket.gethostbyname(sock_name)
except:
    ipconfig = Popen(['ipconfig', 'getifaddr', 'en0'], stdout=PIPE, stderr=PIPE)
    ipconfig, err = ipconfig.communicate()
    ipconfig = ipconfig.decode('utf-8').strip()
    print("socket error")

try:
    urlib = urllib.request.urlopen('http://ipecho.net/plain').read().decode('utf-8')
except:
    urlib = "Error"
    print("urlib error")

try:
    cur = Popen(['curl', '-s', 'https://freegeoip.app/json/' , 'localhost'], stdout=PIPE, stderr=PIPE)
    cur, err = cur.communicate()
    cur = json.loads(cur)
    lat = str(cur["latitude"])
    lon = str(cur["longitude"])
    city = cur["city"]
    cur = cur["ip"]
except:
    lat = lon = city = cur = "Error"
    print("curl error")

try:
    dig = Popen(['dig', '+short', 'myip.opendns.com', '@resolver1.opendns.com'], stdout=PIPE, stderr=PIPE)
    dig, err = dig.communicate()
    dig = dig.decode('utf-8').strip()
except:
    dig = "Error"
    print("dig error")

try:
    pnp = Popen(['upnpc', '-s'], stdout=PIPE, stderr=PIPE)
    pnp, err = pnp.communicate()
    pnp = pnp.decode('utf-8')
    ext_ip = pnp.index("ExternalIPAddress")
    pnp = pnp[(ext_ip + 20) : (ext_ip + 32)]
    pnp = re.match('([0-9]{1,3}\.){3}[0-9]{1,3}', pnp)
    pnp = upnp.group(0)

except:
    print('upnpc error')
    pnp = "Error"


lname = [dt, tt, ssid,  urlib, cur, dig, pnp, ipconfig, sock_name, lat, lon, city]

printer(lname)
printer(lines)
