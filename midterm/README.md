# Midterm Effective Spring 2020
### Cate Lukner

## TASK 1
For task 1, I created directories dir(0-9) using the following command:
```bash
mkdir dir1 dir2 dir3 dir4 dir5 dir6 dir7 dir8 dir9
```

To move each of the files by their last digit into their respective directories, I created a BASH file titled move\_files.sh and it contained the following loop:
```bash
#!/bin/bash

for i in {0..9}
do 
		mv *${i}.txt dir${i}
done
```
The loop moves files based on if their extension is .txt and their last digit matches the current i of the loop. 

## TASK 2

Since I did not want to go through every directory and create the most\_common\_source.txt and most\_common\_dest.txt, I created the following bash script to create those files for me:
```bash
#!/bin/bash

# Create files most_common_source.txt and most_common_dest.txt in each directory
for i in {0..9}
do
                cd ~/Documents/Github/csc221/midterm
                touch dir${i}/most_common_source.txt
                touch dir${i}/most_common_dest.txt
done
```

To place the 10 most common source and dest words from all the files in each directory I created the following bash script named find\_most\_common\_words.sh:
```bash
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
```
Both loops go through the i-th directory. In the i-th directory, awk prints the appropriate column and then pipes it to sort. After sorting, the output is pipped to sed to remove all the extra whitespace. Then sed pipes to unique to get a unique count of each word. After sorting again, head gets the words with the top ten counts. Awk prints the words without the counts then the output is given to the appropriate file. 

## TASK 3

To complete Task 3, I created the following bash script named task3\_loop.sh:
```bash
#!/bin/bash

# Find pairs in each of directories' files that contain most common source words
# Output passed to source.txt in midterm directory
for i in {0..9}
do
		grep -Ff dir${i}/most_common_source.txt dir${i}/*${i}.txt | cut -d ':' -f 2 >> source.txt
done
```
The script uses grep to search each file of the current i-th directory for the words listed in the specified directory's most\_common\_source.txt file. The output of grep is pipped to cut which uses a colon as a delimiter. Cut grabs the second "column" (the column with the pairs) and passes the output to source. This command is run for every directory. 

## TASK 4
To complete Task 4, I copied my command for Task 2 that found the most common source words for each directory. I then modified the command so the most common source word among all of the files in all directories would be found:
```bash
awk '{print $1}' source.txt | sort | sed '/^$/d' | uniq -c | sort -r | head -1 | awk '{print $2}' > most_common_source_word.txt
```
Instead of searching within a specific directory, I had awk search source.txt created in task 3. Instead of having head give the top ten most common source words, I had head only give the first most common source word. 

After running the above command, I ran the following command to find the files with the most common source word:
```bash
awk '$1 == "kornskeppur"{print FILENAME}' dir*/file*.txt | uniq | cut -d '/' -f 2 > most_common_source_files.txt
```
I copied the most common word from most\_common\_source.txt file. After, I had awk test if the first column (the column with the source word) of all the files in any directory starting with 'dir' contained the most common word. All of the files in which awk found the most common word were pipped to uniq. Then, uniq pipped each unique file name to cut to remove the directory in which the file was located. The output from cut put into the file most\_common\_source\_files.txt. 

