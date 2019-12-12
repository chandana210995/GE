#!/bin/sh
echo "Enter the statement"
read statement
echo "Number of redable characters in input text: ${#statement}"
echo -ne "Number of words in input text: $words" 
echo "$statement" | wc -w
lower=${statement,,}
greater=0
total=0
alphabets=0
for i in $lower
do
str=$i
cnt=${#str}

for ((i=0; i < cnt; i++))
do
     char=${str:$i:1}
     if [[ $char == [a-z] ]]
     then
     let alphabets=$alphabets+1
     fi
     count=${lower//[^$char]}
     total=${#count}
     if [ $total > $greater ]
     then
     greater=$total
     fi
done
done
echo "Number of characters in input text that are alphabets: $alphabets"
echo "Number of times the most commonly occuring alphabet occur: $greater"
