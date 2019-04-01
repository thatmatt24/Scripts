#!/usr/local/bin/python3

import subprocess
from subprocess import * 
import datetime
import socket

prip = socket.gethostbyname(socket.gethostname())

pub = subprocess.check_output(['curl', '-s', 'ipecho.net/plain'])


print("Private IP: " + str(prip))

print("Public IP: " + str(pub))

