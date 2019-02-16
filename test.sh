#!/bin/bash

ipa=`ipconfig getifaddr en0`

while [ "$choice" != "q" ]

do

echo " "
echo "**** Common NMAP Commands ****"

echo " "
echo "** For scanning for device's and listing their OS's, choose 'OS'"

echo " "
echo "** For scanning with ..., choose '..'"

echo " "
echo "** For scanning with ..., choose '..'"

echo " "
echo "** To quit, choose 'q'"

read choice

if [ "$choice" == "OS" ];
	then 
	nmap -O $ipa

done

## I should really do this in python, so I can use try/catch blocks and better loops. The trick 
### will be to use command line functions in a python script. That should be possible, right?

