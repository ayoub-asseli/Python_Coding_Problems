"""
To complete this challenge, write a function that accepts a number as a parameter. 
The function should return a number that’s the difference between the largest and 
smallest numbers that the digits can form in the number.
For example, if the parameter is "213", the function should return "198", 
which is the result of 123 subtracted from 321.
"""

import itertools

def rearrange_the_number(number):
	permutations = list(map(lambda x: int(''.join(x)) ,itertools.permutations(str(number))))
	return max(permutations) - min(permutations)

print(rearrange_the_number(12282121212))
