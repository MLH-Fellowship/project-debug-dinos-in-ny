
#CHALLENGE 2

#!/bin/bash
if [ -e $1 ]
num = ls -d *$1* | wc -l
then
    echo 'Found $num matches'
    echo readlink -$1
else
then
    echo 'Found 0 matches'
fi

##

ls -d *$1* | wc -l

##

wc -l to count lines

#CHALLENGE 3

#!/bin/bash

$1
while [ $? -eq 0 ]; do
    $1
done



#CHALLENGE 4

#!/bin/bash

curl -o text.txt https://www.cryptingup.com/api/markets

tr -c '[:alnum:]' '[\n*]' < text.txt | sort | uniq -c | sort -nr | head -10



