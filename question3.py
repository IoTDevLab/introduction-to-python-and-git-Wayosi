#!/usr/bin/env python3

#Name: Quao Nartey-Wayo Emmanuel
#Index Number:PS/ITC/14/0020

import sys

def convertToBinary (number):
     decimal = int(number)
     print (decimal, "in binary = ",bin(decimal) )

if __name__ =='__main__':
     for arg in sys.argv[1:]:
         convertToBinary(arg)
