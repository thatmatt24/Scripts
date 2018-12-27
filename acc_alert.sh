#!/bin/bash

## this checks the access time of the given file and sees if its been accessed since last check
### if it has, then and the owner is alerted and a log of the event is stored, and access time is updated

file=$1
curr="$(date '+%s')"
## access time for $file
eval `stat -s $file`
a_time="$(echo $st_atime)"

## put the access time with filename in a history file and print out file for reference

echo "$file $a_time" >>acc_hist

#debug check
#cat acc_hist.txt

## checks for $file and returns the number next to it

rt_acc=$(awk '/'$file'/{print $NF}' acc_hist)

#debug check
#echo "$rt_acc return"

## now if the checked access time does not equal the historical access time,
### then we know it was accessed since last check
#### now a notification alert will appear with accessed filename


#set DATE for reference if file was accessed
DATE=`date '+%Y-%m-%d %H:%M:%S'`


if [ "$a_time" -ne "$rt_acc" ];
	
	then 
	osascript -e 'display notification "$file accessed" with title "Alert!"';
	echo "File $file accessed on $DATE" >>log_file	

else 
	echo not;

fi


## clear acc_hist

echo >acc_hist
