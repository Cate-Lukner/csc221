#!/bin/bash
#directory analysis

name='etc'
cd ~/../../etc
echo How many files are in directory $name?
ls -l | wc -l 

echo How many directories in $name?
ls -d */ | wc -l

echo What is the biggest file?
du -a ./ |sort -n -r | head -n 1

echo What is the most recently modified or created file?
ls -ltrh | sed -n '2p'| tail -1 

echo List of people who own files in the directory:
find ./ -printf '%u\n' 2>/dev/null | sort -u
