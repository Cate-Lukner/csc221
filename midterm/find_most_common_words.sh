#!/bin/bash

# find most common source words for each file
for i in {0..9}
do
	awk '{print $1}' dir${i}/*.txt | sort | sed '/^$/d' | uniq -c | sort -r | head -10 | awk '{print $2}' > dir${i}/most_common_source.txt
done

# Find most common dest words for each file
for i in {0..9}
do
	awk '{print $2}' dir${i}/*.txt | sort | sed '/^$/d' | uniq -c | sort -r | head -10 | awk '{print $2}' > dir${i}/most_common_dest.txt
done

