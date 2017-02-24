#!usr/bin/env python3

#Name: Quao Nartey-wayo Emmanuel
#Index Number: PS/ITC/14/0020

#create array to store the numbers temporarily
num_list=[]

#check for numbers within the range that satisfy the conditions given
for number in range (1000, 7001):
     if (number%7==0) and (number%5!=0):

#add the required numbers to the 'num_list' array
          num_list.append(str(number))

#print out the numbers stored temporarily in the array
print (','.join(num_list))
