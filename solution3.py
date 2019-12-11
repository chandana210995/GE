import re
statement=input("Enter the statement\n")
print ("Number of redable characters in input text:\0",len(statement))
print ("Number of words in input text:\0",len(statement.split()))
total=0
temp=''
statement=statement.lower()
count=0
for i in range(len(statement)):
    temp=statement[i]
    if temp.isalpha() and len(re.findall(temp,statement))>count:
        count=len(re.findall(temp,statement))
    if statement[i].isalpha():
        total=total+1
print ("Number of characters in input text that are alphabets:\0",total)
print ("Number of times the most commonly occuring alphabet occur:\0",count)
