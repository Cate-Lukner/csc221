#!/bin/bash

# Go to the part 2 directory using an absolute path
cd ~/Documents/Github/csc221/hw3/part2

# TASK 1
# Sort the file shuffled-words.txt
sort shuffled-words.txt > shuffled-words-sorted.txt

# TASK 2
# Produce list of 10 most common words and save to common-words.txt
sort rand-words.txt | uniq -c | sort -r | head -10 > common-words.txt

# TASK 3 
# Produce list of 10 most common numbers and save to common-numbers.txt
sort rand-numbers.txt | uniq -c | sort -r | head -10 > common-numbers.txt

# Task 4
# Produce list of 10 most common number pairs and place in common-2.txt
sort rand-numbers-2.txt | uniq -c | sort -r | head -10 > common-2.txt

# Task 5
# 1,2,3 Top Ten Common Number Triples:
echo Columns 1,2,3 Top Ten Common Number Triples: > common-5.txt
awk '{print $1,$2,$3}' rand-numbers-5.txt | sort -k 1 | uniq -c | sort -r | head -10 >> common-5.txt

# 2,3,4 Top Ten Common Number Triples:
echo -e "\nColumns 2,3,4 Top Ten Common Number Triples:" >> common-5.txt
awk '{print $2,$3,$4}' rand-numbers-5.txt | sort -k 1 | uniq -c | sort -r | head -10 >> common-5.txt

# 3,4,5 Top Ten Common Number Triples:
echo -e "\nColumns 3,4,5 Top Ten Common Number Triples:" >> common-5.txt
awk '{print $3,$4,$5}' rand-numbers-5.txt | sort -k 1 | uniq -c | sort -r | head -10 >> common-5.txt


# 1,3,4 Top Ten Common Number Triples:
echo -e "\nColumns 1,3,4 Top Ten Common Number Triples:" >> common-5.txt
awk '{print $1,$3,$4}' rand-numbers-5.txt | sort -k 1 | uniq -c | sort -r | head -10 >> common-5.txt


# 1,4,5 Top Ten Common Number Triples:
echo -e "\nColumns 1,4,5 Top Ten Common Number Triples:" >> common-5.txt
awk '{print $1,$4,$5}' rand-numbers-5.txt | sort -k 1 | uniq -c | sort -r | head -10 >> common-5.txt


# 1,3,5 Top Ten Common Number Triples:
echo -e "\nColumns 1,3,5 Top Ten Common Number Triples:" >> common-5.txt
awk '{print $1,$3,$5}' rand-numbers-5.txt | sort -k 1 | uniq -c | sort -r | head -10 >> common-5.txt


# 2,4,5 Top Ten Common Number Triples:
echo -e "\nColumns 2,4,5 Top Ten Common Number Triples:" >> common-5.txt
awk '{print $2,$4,$5}' rand-numbers-5.txt | sort -k 1 | uniq -c | sort -r | head -10 >> common-5.txt


