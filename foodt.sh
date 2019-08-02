#!/bin/bash

mon=$(date -v+Mon "+%B %-d" | cut -d" " -f 1,2)
echo $mon
nex=$(date -v+Mon -v+7d "+%B %-d" | cut -d" " -f 1,2)
# echo $nex

list="$(wget -qO -  https://www.ahec.edu/campus-info/food/food-trucks | grep -A 12 "$mon" | grep -B 12 "$nex" | grep "http" | cut -d '"' -f 2)"


printf "\n--------\n$list\n--------\n\n"

# checking each url listed to see if '/menu' is part of it
for site in $list; do
	echo "Checking $site ..."
	if [[ $site == *"pages"* ]]; then
		site="$(echo $site | cut -d/ -f 7)"
		site="www.$site.com"
		site="${site//-}"
		site="${site//[0-9]}"		
	elif [[ $site == *"facebook"* ]]; then
		site="www.$(echo $site | cut -d/ -f 4).com"
	fi

	if [[ $site != *"menu"* ]]; then
		echo "Searching for menu..."
		
		new="$site/menu/"
		try="$(wget -q -O - $new | egrep '[Vv][Ee][Gg][Aa][Nn]')"
		
		if [ ! -z "$try" ]; then
			plural="$site/menus/"
			plural="$(wget -q -O - $plural | egrep '[Vv][Ee][Gg][Aa][Nn]')"
			
			if [ ! -z "$plural" ]; then
			
				truckmenu="$site/food-truck-menu"
				truckmenu="$(wget -q -O - $truckmenu | egrep '[Vv][Ee][Gg][Aa][Nn]')"
				
				if [ ! -z "$truckmenu" ]; then
			
					ourmenu="$site/our-menu"
					ourmenu="$(wget -q -O - $ourmenu | egrep '[Vv][Ee][Gg][Aa][Nn]')"

					if [ ! -z "$ourmenu" ]; then

					echo ":("

					else
						name="$(echo $site | cut -d/ -f3 | cut -d. -f 1 | tr a-z A-Z)"
						echo "Site is $site"
						echo "yay! $name ($site) has vegan options"
					fi
					
					echo ":("

                    else
                  		name="$(echo $site | cut -d/ -f3 | cut -d. -f 1 | tr a-z A-Z)"
						echo "yay! $name ($site) has vegan options"
				fi

				echo ":("

                    else
						name="$(echo $site | cut -d/ -f2 | cut -d. -f 1 | tr a-z A-Z)"
						echo "yay! $name ($site) has vegan options"

			fi
		
		else 

			echo "Found menu, checking options..."

			output="$(wget -qO - $site | egrep '[Vv][eE][gG][aA][nN]')"
			
			if [ ! -z "$output" ];
				then 
					name="$(echo $site | cut -d/ -f3 | cut -d. -f 1 | tr a-z A-Z)"
					echo "yay! $name ($site) has vegan options"

				else

					about="$site/about"
					about="$(wget -qO - $about | egrep '[Vv][Ee][Gg][Aa][Nn]')"
						
					if [ ! -z "$about" ]; then
						name="$(echo $site | cut -d/ -f3 | cut -d. -f 1 | tr a-z A-Z)"
						echo "yay! $name ($site) has vegan options"

					else	
						echo ":("

					fi

			fi

		fi

		printf "\n--------------------\n"
	fi

done

