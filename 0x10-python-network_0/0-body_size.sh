#!/usr/bin/python3
#Bash script that takes in a URL, sends a request to that URL

Curl -ls "$1" | grep -W 'content-length' | cut -f2 -d' '
