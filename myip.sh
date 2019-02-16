#!/bin/bash

priv_ip=`ipconfig getifaddr en0`

pub_ip1="$(dig +short myip.opendns.com @resolver1.opendns.com)"

#pub_ip2=`wget http://ipecho.net/plain -O - -q ; echo`

#pub_ip3=`curl ipecho.net/plain`

echo $pub_ip

if [ "$pub_ip" == "$priv_ip1" ];

	then
	echo $priv_ip2;
else 
	echo $priv_ip1
fi 

## make this check for each and return whichever != pub_ip. If none do, echo "note" and find out why (UDP vs TCP) in order to 
### investigate that network further



