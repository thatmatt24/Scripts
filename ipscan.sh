#!/bin/bash


## grabs private ip address and cuts off host 
#addr_range="`ipconfig getifaddr en0| cut -d . -f 1-3`.*"

#ipaddr=`ifconfig en0 | awk '$1=="inet" {print $2}'`
ipaddr="$(ipcalc `ipconfig getifaddr en0` | cut -d' ' -f 4 | sed -n '5 p')"
echo $ipaddr

while [ "$option" != "q" ]; 
do

	echo "Enter option ([i]pcalc, [n]map, [q]uit): "
	read option

	if [ "$option" == "i" ]
	then
		ipcalc $ipaddr

	elif [ "$option" == "n" ]
	
	then
		echo "nmap options (-[O],-[s]n, or [a]t4): "

		read nmOpt
		
		if [ "$nmOpt" == "O" ]

		then
			echo "nmap -O" 
			sudo nmap -O $ipaddr
		
		elif [ "$nmOpt" == "s" ];
			then
			sudo nmap -sn $ipaddr

		elif [ "$nmOpt" == "a" ];
		then
			sudo nmap -AT4 $ipaddr
		else
			exit
		fi

	else 
		exit
	fi
done
