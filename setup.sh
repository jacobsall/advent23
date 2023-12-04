#!/bin/bash

day=$(date +"%-d")
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
    echo "day already dowloaded, only updating puzzle.md"
    rm -rf puzzles/$day.md
    aoc download -P -p puzzles/$day.md
  else
    echo "creating day $day"
    aoc download -i inputs/$day.txt -p puzzles/$day.md
    testData=$(ggrep -zPo '(?<=\`\`\`\n)[\s\S]*(?=\n\`\`\`)' puzzles/$day.md)
    touch $day.py
    printf "f = open(\"inputs/$day.txt\")\ndata = f.read().strip()\n\ntest_data = \"\"\"\n$testData\n\"\"\".strip()\n\ndef process(data):\n  return data\n\ndef part1(data):\n  return \"not implemented\"\n\ndef part2(data):\n  return \"not implemented\"\n\nprocessed = process(test_data)\nprint(\"part 1\", part1(processed))\nprint(\"part 2\", part2(processed))" >> $day.py
    code puzzles/$day.md $day.py inputs/$day.txt
  fi 
fi
