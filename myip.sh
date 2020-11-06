#!/bin/bash

priv_ip=`ipconfig getifaddr en0`

priv_ip2=`ifconfig en0 | awk '$1=="inet" {print $2}'`

pub_ip1="$(dig -4 +short myip.opendns.com @resolver1.opendns.com)"

pub_ip2=`wget http://ipecho.net/plain -O - -q ; echo`

pub_ip3="$(curl -4s ifconfig.co)"

if [ -n "$pub_ip1" ]; then
	echo "External IP(d): $pub_ip1"

elif [ -n "$pub_ip2" ];	then
	echo "External IP(w): $pub_ip2"

else
	echo "External IP(c): $pub_ip3"

fi

if [ "$pub_ip1" == "$priv_ip" ];

	then
	echo "Internal IP:    $priv_ip2"
else 
	echo "Internal IP:    $priv_ip"
fi 

loc=$(curl -s https://freegeoip.app/csv/ localhost)

vpn="$(nettop -L1 -p 'CyberGhost VPN' | grep ipsec)"


if [ -z "$vpn"  ]; then
	vpn_status="Inactive"
	echo "VPN is inactive"

	else
		vpn_status="Active"
		echo "VPN is active"

fi

ip=$(echo $loc | cut -d, -f 1)
city=$(echo $loc | cut -d, -f 6)
lat=$(echo $loc | cut -d, -f 9)
long=$(echo $loc | cut -d, -f 10)
dat=$(date "+%Y-%m-%d, %H:%M:%S")

echo "$dat; $ip; $city; $lat, $long; $vpn_status" >> /Users/mattmcmahon/Desktop/repos/Scripts/ip-log.nosync
