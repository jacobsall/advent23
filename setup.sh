#!/bin/bash

day=$(date +"%d")
delete=false

while getopts 'rd:' o; do
  case "${o}" in
    d)
      day=$OPTARG
    ;;
    r) 
      delete=true
    ;;
  esac
done

if $delete ; then
  echo "deleting day $day"
  rm -rf inputs/$day.txt
  rm -rf puzzles/$day.md
  rm -rf $day.py
else 
  if test -f "inputs/$day.txt"; then
    echo "day already dowloaded, skipping"
  else
    echo "creating day $day"
    aoc download -i inputs/$day.txt -p puzzles/$day.md
    touch $day.py
    printf "f = open(\"inputs/$day.txt\")\ndata = f.read()\n" >> $day.py
    code puzzles/$day.md $day.py inputs/$day.txt
  fi 
fi
