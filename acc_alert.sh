
#!/bin/bash

## this checks the access time of the given file and sees if its been accessed since last check
### if it has, then it iterates a count amd stores it based on the filename, and then updates the access time

#variables
file=$1
curr="$(date '+%s')"
eval `stat -s $file`
a_time="$(echo $st_atime)"
count="$(cat counter.txt)"
a=1
echo file
echo $file

#for debug
##echo $st_atime  
echo "file time: $a_time"
echo "system time: $curr"

## put the access time with filename in a history file and print out file for reference

echo "$file $a_time" >>acc_hist.txt

#debug check
#cat acc_hist.txt

## now I need something that can check for $file and return the number next to it

rt_acc=$(awk '/'$file'/{print $NF}' acc_hist.txt)

#debug check
echo "$rt_acc return"

## now if the checked access time does not equal the historical access time,
### then we know it was accessed since last check
#### so we can iterate the count (passing it to the count file), and update the access time history

echo DEBUG
echo $a_time
echo $rt_acc

if [ "$a_time" -ne "$rt_acc" ];
	
	then echo $((count + a)) >counter.txt;

else 
	echo not;

fi


cat counter.txt

## will need a part that updates the a_time in acc_hist.txt


