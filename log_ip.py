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
    
    for i in list:

        if ("----" in i):
            i = '{:^17}'.format(i)
            file.write('|' + i)
        elif (i == list[len(list) - 1]):
            i = '{:^17}'.format(i)
            file.write('|' + i + '|')
        elif ( i == socket.gethostname() or i == "sock_hostname"):
            i = '{:^25}'.format(i)
            file.write('|' + i)
        else:
            i = '{:^17}'.format(i)
            file.write('|' + i)

    file.write("\n")
    file.close()


# example for formating:
title = ['date', 'time', 'ext: urllib', 'ext: curl', 'ext: dig', 'ext: upnpc', 'internal', 'sock_hostname', 'latitude', 'longitude', 'city']
lines = ['-----------------','-----------------','-----------------','-----------------','-----------------','-----------------','-----------------','-------------------------','-----------------','-----------------','-----------------|']
# printer(lines)
# printer(title)
printer(lines)

dt = datetime.datetime.now().strftime("%b %d %Y")
tt = datetime.datetime.now().strftime("%H:%M:%S")

try:
    ipconfig = socket.gethostbyname(socket.gethostname())
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
    lat, lon, city, cur = "Error"
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
    pnp = re.findall(r'ExternalIPAddress', pnp)[0].split()[1]

except:
    print('upnpc error')
    pnp = "Error"


lname = [dt, tt, urlib, cur, dig, pnp, ipconfig, socket.gethostname(), lat, lon, city]

printer(lname)
printer(lines)


