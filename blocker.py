#!/usr/local/bin/python3

import datetime
from subprocess import *

x=datetime.datetime.now()
filename = x.strftime("%d.%b.%y-%H:%M:%S") + "_dump.pcap"
Popen(['touch', filename])

tcpd = Popen(['sudo', 'tcpdump', '-w', filename, '-i', 'en0'], stdout=PIPE, stdin=PIPE)

with open('./' + filename) as dump:

	line = dump.readline()

	while(line):
	
		print(line)
		line = dump.readline()


