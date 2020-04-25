# Over the Wire

### Level 0
host: bandit.labs.overthewire.org
port: 2220
username: bandit0
password: bandit0
relevant command: ssh

`ssh -p 2220 bandit0@bandit.labs.overthewire.org`

Solution: boJ9jbbUNNfktd78OOpsqOltutMc3MY1

### Level 1

`cat ./-`

Solution: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

### Level 2

`cat spaces\ in\ this\ filename`

Solution: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

### Level 3
```
cd inhere
ls -a
cat .hidden
```

Solution: pIwrPrtPN36QITSp3EQaw936yaFoFgAB

### Level 4
```
ls
cd inhere
file ./-file*
file ./-file07
```

Solution: koReBOKuIDDepwhWk7jZC0RTdopnAYKh

### Level 5

```
find . -type f -size 1033c
cat ./maybehere07/.file2
```

Solution: DXjZPULLxYr17uwoI01bNLQbtFemEgo7

### Level 6

```
find . -type f -size 33c -group bandit6 -user bandit7 2> dev/null
cat ./var/lib/dpkg/info/bandit7.password
```

Solution: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

### Level 7

```
grep millionth data.txt
```

Solution: cvX2JJa4CFALtqS87jk27qwqGhBM9plV

### Level 8

'''
sort data.txt | uniq -c | sort
'''

Solution: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

### Level 9

```
bandit9@bandit:~$ strings data.txt | grep '====='
2========== the
========== password
========== isa
========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
```

Solution: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

### Level 10

```
bandit10@bandit:~$ base64 -d data.txt
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```

Solution: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

### Level 11

```
bandit11@bandit:~$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-z'
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
```

Solution: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

### Level 12

```
bandit12@bandit:/tmp/tmp.CqiVxyoiCp$ alias untar="tar -xOf - --wildcards '*.bin'" 
bandit12@bandit:/tmp/tmp.CqiVxyoiCp$ cat data.txt | xxd -r - | zcat | bzcat | zcat | untar | untar | bzcat | untar | zcat > output.bin
bandit12@bandit:/tmp/tmp.CqiVxyoiCp$ cat output.bin
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```

Solution: 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

### Level 13

```
bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost
```

Solution: command above

### Level 14
