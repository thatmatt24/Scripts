#!/bin/bash

#nmap -sP "`ipconfig getifaddr en0 | cut -d. -f 1-3`.*" | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b"


printf "\nGrep-ing IP's from netstat...\n" 

netstat -tulpn | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" >> file & 
cat $file 
