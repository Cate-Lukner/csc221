#!/bin/bash

# Create files most_common_source.txt and most_common_dest.txt in each directory
for i in {0..9}
do
		cd ~/Documents/Github/csc221/midterm
		touch dir${i}/most_common_source.txt
		touch dir${i}/most_common_dest.txt
done
