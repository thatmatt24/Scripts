#!/bin/bash


## grabs private ip address and cuts off host 
addr_range="`ipconfig getifaddr en0| cut -d . -f 1-3`.*"

echo $addr_range

ipaddr=`ifconfig en0 | awk '$1=="inet" {print $2}'`


while [ "$option" != "quit" ]; do

	echo "Enter option (ipcalc, nmap, quit):"
	read option

	if [ "$option" == "ipcalc" ];

		then
		ipcalc $ipaddr;

	elif [ "$option" == "nmap" ];
	
		then
		echo "nmap options (-O,-sn, or both?):"

		read nmOpt
		
		if [ "$nmOpt" == "-O" ];

			then
			echo "nmap -O 
			nmap -O $addr_range;
		
		elif [ "$nmOpt" == "-sn" ];
			then
			nmap -sn $addr_range;

		elif [ "$nmOpt" == "both" ];
			then
			nmap -Osn $addr_range;
		
		fi

	fi
done
