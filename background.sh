#!/bin/zsh
i=0
cd /home/dracul/programing/python/system_hacks/
while [[ ! "$i" -eq 1 ]]
do
  python -m background
  nitrogen --restore
  sleep 120
done
