#!/bin/bash


## grabs private ip address and cuts off host 
addr_range="`ipconfig getifaddr en0| cut -d . -f 1-3`.*"

echo $addr_range



