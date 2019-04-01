#!/bin/bash

#w="$(date +%w)"
#diff=$(( (8-$w)%7 ))
#[[ $diff -eq 0 ]] && diff=7
#mon="$(date -v+${diff}d "+%B %d" | tr a-z A-Z)"

mon=$(date -v+Mon "+%B %-d" | cut -d" " -f 1,2 | tr a-z A-z)
echo $mon

list="$(wget -q -O - https://www.ahec.edu/campus-info/food/food-trucks | grep -A 12 "FOOD TRUCK LINE UP" |
			 grep -B 12 "$mon" | grep "http" | cut -d '"' -f 2)"


printf "\n--------\n$list\n--------\n\n"

# checking each url listed to see if '/menu' is part of it
for i in $list; do
	echo "*Checking $i..."
	if [[ $i != *"menu"* ]]; then
		echo "No menu, doing more digging..."
		
		new="$i/menu/"
		try="$(wget -q -O - $new | egrep '[Vv][Ee][Gg][Aa][Nn]')"
		
		if [ ! -z "$try" ]; then
			
			echo ":("
		else 

			echo "Has menu, checking options..."

			output="$(wget -q -O - $i | egrep '[Vv][eE][gG][aA][nN]')"
		
			echo "$output"
	
			if [ ! -z "$output" ];
				then 
		
					echo "yay! $i has vegan options"

				else
		
					echo ":("
			fi

		fi

		printf "\n--------------------\n"
	fi
done

