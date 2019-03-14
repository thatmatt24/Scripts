#!/bin/bash

priv_ip=`ipconfig getifaddr en0`

pub_ip1="$(dig +short myip.opendns.com @resolver1.opendns.com)"

pub_ip2=`wget http://ipecho.net/plain -O - -q ; echo`

#pub_ip3=`curl ipecho.net/plain`

echo "Public IP is $pub_ip1"

if [ "$pub_ip1" == "$priv_ip" ];

	then
	echo "Private IP is $priv_ip2"
else 
	echo "Private IP is $priv_ip"
fi 

## make this check for each and return whichever != pub_ip. If none do, echo "note" and find out why (UDP vs TCP) in order to 
### investigate that network further



