#!/bin/bash

# command to create directories named that word
cd ~/Documents/Github/csc221/hw3/
# have a list with all the words
words=(
 dawdy
 loudness
 reallots
 salopette
 special
 specificity
 submultiple
 swum
 unprejudicated
 vivificate
)
for i in "${words[@]}"
do
		mkdir $i
		echo made $i

done

files=(part1/*)
for i in "${words[@]}"
do
		for j in "${files[@]}"
		do
			if grep -Fxq "$i" $j
			then
				mv $j $i
				echo moved $j to $i
			else
				echo no $i in $j 
			fi
		done
done

for i in "${words[@]}"
do
		rm -d $i
		echo removed $i
done
# have a loop that loops over the list of words
# if statement that tests for a word in a file
