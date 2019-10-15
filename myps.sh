#!/bin/bash

me="$(who am i | cut -d" " -f 2)"

ps -t $me | awk '!/login/ && !/ps -t/ && !/-bash/ {print}'


for line in $(ps -t $me | tail +2 | awk '!/login/ && !/ps -t/ && !/-bash/ {print $1}'); do
  read -p "Kill ${line}? " -n 1 -r 
  echo    # (optional) move to a new line
  if [[ $REPLY =~ ^[Yy]$ ]]
  then
    
    sudo kill -9 $(echo ${line} | cut -d: -f 1)
  fi

done
