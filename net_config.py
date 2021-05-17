# log internal ip's from (2) sources: ipconfig, upnpc
# log external ip's from (4) sources: urllib, curl, dig, upnpc
# print these into formatted columns for comparison and verification (pending csv or json)

################
#### TODO's ####
# -- rewrite as clean/readable/efficient code
# -- multithreading (pending bug fixes)
# -- run when wifi connection made (automator)
#       --- if connection is same as previous do not run nor if connection has been previously logged in the past 30 days
# -- add logging
# -- add router manufacturer info (crontab for monthly refresh)
# -- account for 'arp-scan' running and not timing out (ie IllegalPetes WiFi)
#       --- identify other bugs that need addressing or investigating
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
        3: 35,
        9: 25,
        10: 14,
        11: 16,
        12: 17
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
# title = ['date', 'time', 'SSID', 'Router Type', 'ext: urllib', 'ext: curl', 'ext: dig', 'ext: upnpc', 'internal', 'sock_hostname', 'latitude', 'longitude', 'city']
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
    # print(socket.getsockname())
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


#Router Manufacturer from MAC address
    
try:
    #get router IP
    router_ip = Popen('netstat -rn | grep default', shell=True, stdout=PIPE, stderr=PIPE)
    router_ip, err = router_ip.communicate()
    router_ip = router_ip.decode('utf-8')
    router_ip = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", router_ip)[0]
    # router_ip = str(router_ip)
    print(router_ip)

    #get MAC address
    router = Popen(['arp-scan', '-l'], stdout=PIPE, stderr=PIPE)
    router, err = router.communicate()
    router = router.decode('utf-8')
    router = router.split(router_ip)[1].split("\n")[0:1] 
    router = router[0].split("\t")[1].split(":")[0:3]
    router[0:3] = [''.join(router[0:3])]
    router = router[0].replace(":", "").upper()
    # print(router)

    with open('/usr/local/Cellar/arp-scan/1.9.5_1/share/arp-scan/ieee-oui.txt','r') as mac:
        for line in mac:
            if router in line:
                router_mac = line.split(router)[1].strip()
                # print(match)
            else:
                print("No OUI match")

    if not router_mac:
        router_mac = "N/A"


except:
    print("MAC error - manufacturer not found")
    router_mac = "error"


printer([dt, tt, ssid, router_mac, urlib, cur, dig, pnp, ipconfig, sock_name, lat, lon, city])
