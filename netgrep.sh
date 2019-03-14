#!/bin/bash

#nmap -sP "`ipconfig getifaddr en0 | cut -d. -f 1-3`.*" | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b"

rm opipe
rm ipipe

printf "\nGrep-ing IP's from netstat...\n" 

mkfifo ipipe
mkfifo opipe
 
netstat > ipipe & 
grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" ipipe > opipe &
sort -u opipe > opipe
cat opipe
 
rm opipe
rm ipipe

 
