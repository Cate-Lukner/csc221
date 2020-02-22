# Homework 03: Bash File System and Redirection
### Cate Lukner

## PART 1

The Bash Script is located for your reference in the directory hw3/ named "sort_files.sh".
Here is my break down my BASH script:

1. Let the operating system know this is a bash script:
```bash
#!/bin/bash
```
2. Navigate to the desired directory, in this case, the hw3 directory
```bash
cd ~/Documents/Github/csc221/hw3
```
3. Create an array of my assigned given words. To create this array, I simply 
yanked the words from the README file and pasted them in the BASH script. I 
assigned this array to the name "words" for later reference.
```bash
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
```
4. Next, I created a for loop that would iterate over the "words" array and for each
word in the "words" array, it would create a directory named that word. It would
then echo a confirmation that that directory was created. 
```bash
for i in "${words[@]}"
do
		mkdir $i
		echo made $i

done
```
5. Now, I needed an array with all the file names in part1 directory. To create this
array, I assigned the name "files" to an array created using "part/\*", which asks for 
all the file names in the part1 directory.
```bash
files=(part1/*)
```
6. Finally, I created a for loop which would iterate over every word in the "words" 
array. For each word in the "words" list, there was another for loop that would 
iterate over every file in the part1/ directory and search for the word. If the word
was found then the file would be moved to the previously created directory in hw3/ 
named that word. If no word was found, the the loop would move onto the next word in 
the "words" array. 
```bash
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
```


## PART 2:

The full bash file for your reference is named "part2_tasks_script.sh"
Here is the break-down of my BASH script and my solutions for each task:

1. Let the operating system know this is a bash file. Then go to part2/ 
directory using an absolute path:
```bash
#!/bin/bash

cd ~/Documents/Github/csc221/hw3/part2
```
2. Task one asks to sort all the words in a file and place in the 
file named shuffled-words-sorted.txt. I used the sort command then
directed the output of the sort command to an output file named
shuffled-words-sorted.txt. 
```bash
sort shuffled-words.txt > shuffled-words-sorted.txt
```
3. Task 2 asks to produce a list of the ten most common words and save
to a specific file name. To do this, I sorted the rand-words.txt file
using the sort command and pipped it to the uniq command with the -c flag.
I then pipped the output of the uniq command to sort again, which would now
sort by the count of occurances. I pipped the second sort command output to
head so I could get the top ten most commond words, and I had this output
be written to the file named common-words.txt. 
```bash
sort rand-words.txt | uniq -c | sort -r | head -10 > common-words.txt
```
4. Task three is a similar command to task two, with the only exception of the
file names being changed and the commands sorting numbers instead of words. I used 
the file rand-numbers.txt and placed the desired output into the file named 
commmon-numbers.txt. 
```bash
sort rand-numbers.txt | uniq -c | sort -r | head -10 > common-numbers.txt
```
5. Task four was similar to tasks two and three, explained in steps 3 and 4.
I only had to change the file names to starting with file rand-numbers-2.txt
and the output file name to be common-2.txt. In task 4, the command was sorting
pairs of numbers rather than just single numbers or words. 
```bash
sort rand-numbers-2.txt | uniq -c | sort -r | head -10 > common-2.txt
```
6. For task 5, I used awk to print the columns for each specified column subsection
in the file rand-numbers-5.txt. I then passed awk's output to sort, which then sorted
by the first column of the subselected columns. The output from sort was pipped to 
uniq with the -c flag to get a count of each unique triple. The counts of the triples
were sorted from highest to lowest then pipped into the head command so head could get
the top ten triples. These top ten triples were then written into the output file named
common-5.txt. In common-5.txt, I delimited each top ten of the subselections writting in
common-5.txt an output from echo. 

```bash
echo Columns 1,2,3 Top Ten Common Number Triples: > common-5.txt
awk '{print $1,$2,$3}' rand-numbers-5.txt | sort -k 1 | uniq -c | sort -r | head -10 >> common-5.txt

echo -e "\nColumns 2,3,4 Top Ten Common Number Triples:" >> common-5.txt
awk '{print $2,$3,$4}' rand-numbers-5.txt | sort -k 1 | uniq -c | sort -r | head -10 >> common-5.txt

echo -e "\nColumns 3,4,5 Top Ten Common Number Triples:" >> common-5.txt
awk '{print $3,$4,$5}' rand-numbers-5.txt | sort -k 1 | uniq -c | sort -r | head -10 >> common-5.txt

echo -e "\nColumns 1,3,4 Top Ten Common Number Triples:" >> common-5.txt
awk '{print $1,$3,$4}' rand-numbers-5.txt | sort -k 1 | uniq -c | sort -r | head -10 >> common-5.txt

echo -e "\nColumns 1,4,5 Top Ten Common Number Triples:" >> common-5.txt
awk '{print $1,$4,$5}' rand-numbers-5.txt | sort -k 1 | uniq -c | sort -r | head -10 >> common-5.txt

echo -e "\nColumns 1,3,5 Top Ten Common Number Triples:" >> common-5.txt
awk '{print $1,$3,$5}' rand-numbers-5.txt | sort -k 1 | uniq -c | sort -r | head -10 >> common-5.txt

echo -e "\nColumns 2,4,5 Top Ten Common Number Triples:" >> common-5.txt
awk '{print $2,$4,$5}' rand-numbers-5.txt | sort -k 1 | uniq -c | sort -r | head -10 >> common-5.txt
```


