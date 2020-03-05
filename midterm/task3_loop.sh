#!/bin/bash

# Find pairs in each of directories' files that contain most common source words
# Output passed to source.txt in midterm directory
for i in {0..9}
do
		grep -Ff dir${i}/most_common_source.txt dir${i}/*${i}.txt | cut -d ':' -f 2 >> source.txt
done
