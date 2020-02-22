
Your lab directory is: C:\Users\catlu\Documents\Github\csc221\hw3

Inside your lab directory, you must create these directories:

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

For example:

$ cd C:\Users\catlu\Documents\Github\csc221\hw3
$ mkdir dawdy

These directories are random words chosen based on your username.

Each file in your lab directory (e.g. file00000) contains a list of
random words, but each one contains one instance of each of the random
words you used to create your directories.

Each file must be placed in the directory whose name is contained in
the file.

E.g. if the word "dawdy" is in the file "file00000", then you must move
that file "file00000" into the directory "dawdy".

$ cd C:\Users\catlu\Documents\Github\csc221\hw3
$ mv file00000 dawdy

This is the full BASH script I created to handle the assigned tasks:

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


Now let's break down the BASH script:

1. Let the operating system know this is a bash script:
#!/bin/bash

2. Navigate to the desired directory, in this case, the hw3 directory
cd ~/Documents/Github/csc221/hw3

3. Create an array of my assigned given words. To create this array, I simply 
yanked the words from the README file and pasted them in the BASH script. I 
assigned this array to the name "words" for later reference.

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

4. Next, I created a for loop that would iterate over the "words" array and for each
word in the "words" array, it would create a directory named that word. It would
then echo a confirmation that that directory was created. 

for i in "${words[@]}"
do
		mkdir $i
		echo made $i

done

5. Now, I needed an array with all the file names in part1 directory. To create this
array, I assigned the name "files" to an array created using part1/*, which asks for 
all the file names in the part1 directory.

files=(part1/*)

6. Finally, I created a for loop which would iterate over every word in the "words" 
array. For each word in the "words" list, there was another for loop that would 
iterate over every file in the part1/ directory and search for the word. If the word
was found then the file would be moved to the previously created directory in hw3/ 
named that word. If no word was found, the the loop would move onto the next word in 
the "words" array. 

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


