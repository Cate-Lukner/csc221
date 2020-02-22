#!/bin/bash

cd ~/Documents/Github/csc221/hw3/

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

