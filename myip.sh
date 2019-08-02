#!/bin/bash

priv_ip=`ipconfig getifaddr en0`

pub_ip1="$(dig +short myip.opendns.com @resolver1.opendns.com)"

pub_ip2=`wget http://ipecho.net/plain -O - -q ; echo`

#pub_ip3=`curl ipecho.net/plain`

if [ -z "$pub_ip1" ]; 
	then
	echo "External IP(w) is $pub_ip2"

	else
		echo "External IP(d) is $pub_ip1"

fi

if [ "$pub_ip1" == "$priv_ip" ];

	then
	echo "Internal IP is $priv_ip2"
else 
	echo "Internal IP is $priv_ip"
fi 

loc=$(curl -s https://freegeoip.app/csv/ localhost)

if [[ $loc == *"Canada"* ]]; then
	printf "VPN is active\n"

	else
		printf "VPN is inactive\n"

fi

ip=$(echo $loc | cut -d, -f 1)
city=$(echo $loc | cut -d, -f 6)
lat=$(echo $loc | cut -d, -f 9)
long=$(echo $loc | cut -d, -f 10)
dat=$(date)

echo "$ip at $city: $lat, $long on $dat" >> /Users/mattmcmahon/Desktop/Scripts/ip-log.nosync
