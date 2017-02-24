#!/usr/bin/env python3

##Name: Quao Nartey-Wayo Emmanuel
#Index Number:PS/ITC/14/0020


firstNum = 1 
secondNum = 1
total = 0
while firstNum <= 4000000:
     if firstNum % 2 == 0:
         total += firstNum
#code for generating fibonacci sequence
     firstNum, secondNum = secondNum, firstNum + secondNum

print ("The sum of the even-valued terms in the fibonacci sequence less than 4 million is: ")
print (total)
