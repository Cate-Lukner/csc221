#!/bin/bash
# Meant to back up this totally cool fake project I have
# This is by Cate

date=`date +%F`
mkdir ~/fake_project/
touch ~/fake_project/$1
mkdir ~/backup/$1_$date
cp -R ~/fake_project/$1 /backup/$1_$date
echo Backup of $1 completed
