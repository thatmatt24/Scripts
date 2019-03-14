#!/bin/bash

w="$(date +%w)"
diff=$(( (8-$w)%7 ))
[[ $diff -eq 0 ]] && diff=7
mon="$(date -v+${diff}d "+%B %d" | tr a-z A-Z)"
echo $mon

list="$(wget -q -O - https://www.ahec.edu/campus-info/food/food-trucks | grep -A 12 "FOOD TRUCK LINE UP" |
			 grep -B 12 "$mon" | grep "http" | cut -d '"' -f 2)"


printf "\n--------\n$list\n--------\n\n"

for i in $list; do
	printf "*Checking $i...\n"
	if [[ $i != *"menu"* ]]; then
		printf "No menu, doing more digging...\n"
		new="$i/menu/"
#		printf "$new -----------------"
		try="$(wget -q -O - $new | egrep '[Vv][Ee][Gg][Aa][Nn]')"
#		printf "$try ****************\n"
		else 
		printf "Has menu, checking options...\n"
	fi
	
	output="$(wget -q -O - $i | egrep '[Vv][eE][gG][aA][nN]')"
#	printf "$output\n"	
	
	if [ ! -z "$output" ];
		then 
		
		printf "yay! $i has vegan options\n"
		
#		if [ -z "$new" ]; 
#			then
#			if [ ! -z "$try" ]; 
#				then 
#				printf "yay! $i has vegan options\n"
#				else
#				printf ":(\n";
#			fi
#			else
#			printf ":(\n"
#		fi
			else
		
		printf ":(\n"
	fi
	printf "\n--------------------\n"
done
