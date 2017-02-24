#!usr/bin/env python3

#Name: Quao Nartey-wayo Emmanuel
#Index Number: PS/ITC/14/0020


num_list=[]
for number in range (1000, 7001):
     if (number%7==0) and (number%5!=0):
          num_list.append(str(number))
print (','.join(num_list))
