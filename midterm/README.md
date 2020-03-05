# Midterm Effective Spring 2020
### Cate Lukner

## TASK 1
For task 1, I created directories dir(0-9) using the following command:
```bash
mkdir dir1 dir2 dir3 dir4 dir5 dir6 dir7 dir8 dir9
```

To move each of the files by their last digit into their respect directories, I created a BASH file titled move\_files.sh and it contained the following loop:
```bash
#!/bin/bash

for i in {0..9}
do 
		mv *${i}.txt dir${i}
done
```
The loop moves files based on if their extension is .txt and their last digit matches the current i of the loop. 

## TASK 2

To place the 10 most common source and dest words from all the files in each directory I created the following bash script:
```bash
#!/bin/bash

# find most common source words for each file
for i in {0..9}
do
	awk '{print $1}' dir${i}/*.txt | sort -r | uniq -c | sort -r | head -10 | awk '{print $2}' > dir${i}/most_common_source.txt
done

# Find most common dest words for each file
for i in {0..9}
do
	awk '{print $2}' dir${i}/*.txt | sort -r | uniq -c | sort -r | head -10 | awk '{print $2}' > dir${i}/most_common_dest.txt
done
```
Both loops go through the i-th directory. In the i-th directory, awk prints the appropriate column and then pipes it to sort. Sort pipes to unique to get a unique count of each word. After sorting again, head gets the words with the top ten counts. Awk prints the words without the counts then the output is given to the appropriate file. 
