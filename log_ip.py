# log internal ip's from (2) sources: ipconfig, upnpc
# log external ip's from (4) sources: urllib, curl, dig, upnpc
# print these into formatted columns for comparison and verification

################
#### TODO's ####
# -- run when wifi connection made
#       --- if connection is same as previous do not run nor if connection has been previously logged in the past 30 days
# -- copy contents to another file for safe keeping
# -- add logging
# -- add router manufacturer info
# -- add option to record data that was cut off to fit in table
#       --- ie [-n] if socket.gethostname (sock_name) is > 17, can be recorded in separate file and the option do so on runtime
################

from subprocess import *
import datetime
import time
import socket
import urllib.request
import json
import re


def printer(list):
    file = open('/Users/mattmcmahon/Desktop/Scripts/ip-log1.nosync', 'a')

    position_default = 15
    positions = {
        0: 11,
        1: 9,
        2: 12,
        8: 25,
        9: 14,
        10: 16,
        11: 17
    }

    elements = []

    for i,el in enumerate(list):
        pos = positions.get(i, position_default)
        el = el[0:pos]
        el.center(pos, ' ')
        elements.append(el)

    to_write = '\t'.join(elements)
    file.write(to_write)

    file.write("\n")
    file.close()

# example for formating:
# title = ['date', 'time', 'SSID','ext: urllib', 'ext: curl', 'ext: dig', 'ext: upnpc', 'internal', 'sock_hostname', 'latitude', 'longitude', 'city']
# lines = ['--------------', '-----------', '-----------------', '-----------------', '-----------------', '-----------------', '-----------------', '-----------------', '-------------------------', '--------------', '----------------', '-----------------|']
# dt = tt = urlib = cur = dig = pnp = ipconfig = sock_name = lat = lon = city = "test"
# ssid = "-------------------"

# printer(lines)
# printer(title)
# printer(lines)

dt = datetime.datetime.now().strftime("%b.%d.%Y")
tt = datetime.datetime.now().strftime("%H:%M:%S")

try:
    ssid = Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'], stdout=PIPE, stderr=PIPE)
    ssid, err = ssid.communicate()
    ssid = ssid.decode('utf-8')
    ssid = ssid.split("SSID:")[2].split("\n")[0]
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
    pnp = pnp.split("ExternalIPAddress")[1].split(" = ")[1].split("\n")[0]

except:
    print('upnpc error')
    pnp = "Error"


printer([dt, tt, ssid, urlib, cur, dig, pnp, ipconfig, sock_name, lat, lon, city])

## strip newlines and print to terminal
# with open('../ip-log1.nosync', 'r') as f:
#     for line in f.readlines():
#         print(end=line)
#         print(line.rstrip('\n'))
