#!/bin/bash
#
#This script is used to scan specific ports for targets


echo "Enter target IP (First Octet)"

read target_IP1

echo "Enter target IP (Second Octet)"

read target_IP2

echo "Enter Port to Scan"

read port

echo "Enter text file name to save the search"

read text_name

nmap -sT $target_IP1-$target_IP2 -p $port >/dev/null -oG $text_name

cat $text_name | grep open >> $text_name

cat $text_name




