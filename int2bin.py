# Binary Addition

"""
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

"""

def binary_addition(a,b):
    total = (a + b)
    print (total)
    total_bin = (bin(total)[2:])
    print (total_bin)


binary_addition(5,2)


