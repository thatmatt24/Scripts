#!/bin/bash

public="$(dig +short myip.opendns.com @resolver1.opendns.com)"

public2=`wget http://ipecho.net/plain -O - -q ; echo`

priv=`ifconfig en0 | awk '$1=="inet" {print $2}'`

priv2=`ipconfig getifaddr en0`

if [ "$public" == "$public2" ];
	
	then
	code=1 
	pub_ip="$public"
	printf "\nPublic IP = $public\n"

else
	code=2
	pub_ip="$public2"
	printf "\nPublic IP = $public2\n"

fi 


printf "\nComparing nmap output from LAN IP with WAN IP, looking for ports available on both...\n\n"

nmap -T4 -Pn $public

printf "\nEnd of LAN scan.\n \nBeginning WAN scan...\n"

nmap -T4 -Pn -sn $priv

exit 0
